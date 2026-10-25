-- Source notes: move each paragraph's parenthetical citations into one short note at the end of
-- the paragraph. Runs before --citeproc. Narrative citations ("Smith et al. (2024) found") stay in
-- the text; tables and figure captions keep their inline "Source:" citations.

local PAGELINE = os.getenv("SRCMODE") == "pageline"

local function collect(inlines)
  local kept, cites, seen = pandoc.List(), pandoc.List(), {}
  for _, el in ipairs(inlines) do
    local moved = false
    if el.t == "Cite" then
      local all_paren = true
      for _, c in ipairs(el.citations) do
        if c.mode == "AuthorInText" then all_paren = false end
      end
      if all_paren then
        for _, c in ipairs(el.citations) do
          local sig = c.id .. "|" .. pandoc.utils.stringify(c.suffix)
          if not seen[sig] then
            seen[sig] = true
            c.mode = "NormalCitation"
            cites:insert(c)
          end
        end
        moved = true
        -- drop the space that preceded the citation
        if #kept > 0 and (kept[#kept].t == "Space" or kept[#kept].t == "SoftBreak") then
          kept:remove(#kept)
        end
      end
    end
    if not moved and PAGELINE and el.t == "Cite" then
      -- narrative citation: keep the names in the sentence (the year is stripped later),
      -- and list the source with the paragraph's others
      for _, c in ipairs(el.citations) do
        local sig = c.id .. "|" .. pandoc.utils.stringify(c.suffix)
        if not seen[sig] then
          seen[sig] = true
          cites:insert(pandoc.Citation(c.id, "NormalCitation", c.prefix, c.suffix))
        end
      end
      kept:insert(pandoc.Span({el}, {class = "narr"}))
      moved = true
    end
    if not moved then kept:insert(el) end
  end
  return kept, cites
end

local function add_note(el)
  local kept, cites = collect(el.content)
  if #cites == 0 then return nil end
  local cite = pandoc.Cite({pandoc.Str("")}, cites)
  kept:insert(pandoc.Note({pandoc.Plain({pandoc.Span({cite}, {class = "srcnote"})})}))
  el.content = kept
  return el
end

return {{
  traverse = "topdown",
  Table = function(el) return el, false end,
  Figure = function(el) return el, false end,
  Note = function(el) return el, false end,
  Para = function(el) return add_note(el) end,
  Plain = function(el) return add_note(el) end,
}}
