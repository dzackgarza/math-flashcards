-- Pair Pandoc Divs, then delegate rendering and media handling to Ankdown.
-- https://pandoc.org/lua-filters.html#type-div
function Pandoc(doc)
  local pairs_by_id, front_order = {}, {}
  for _, block in ipairs(doc.blocks) do
    if block.t ~= 'Div' then error('A deck must contain Front and Back pairs.') end
    local front = block.classes:includes('front')
    local back = block.classes:includes('back')
    if front == back then error('Each card side needs Front or Back.') end
    local id = block.attributes['card-id']
    if not id or id == '' then error('Each card side needs a card ID.') end
    local side = front and 'front' or 'back'
    local pair = pairs_by_id[id] or {}
    if pair[side] then error('Duplicate ' .. side .. ' for card ' .. id) end
    pair[side] = block
    pairs_by_id[id] = pair
    if front then table.insert(front_order, id) end
  end
  for id, pair in pairs(pairs_by_id) do
    if not pair.front or not pair.back then
      error('Card ' .. id .. ' needs both Front and Back.')
    end
  end
  local items = {}
  if #front_order == 0 and FORMAT == 'plain' then
    io.stdout:write(pandoc.json.encode({
      meta = {
        title = doc.meta.title and pandoc.utils.stringify(doc.meta.title) or 'Ankdown Deck',
        model = doc.meta.model and pandoc.utils.stringify(doc.meta.model) or 'Ankdown Model',
      },
      cards = pandoc.List({}),
    }))
    os.exit(0)
  end
  for _, id in ipairs(front_order) do
    local pair = pairs_by_id[id]
    local front = #pair.front.content > 0 and pandoc.Div(pair.front.content) or pandoc.Para({})
    local back = #pair.back.content > 0 and pandoc.Div(pair.back.content) or pandoc.Para({})
    local item = {front, back}
    local tags = pair.front.attributes.tags
    if tags and tags ~= '' then
      table.insert(item, pandoc.Para({pandoc.Str('tags: ' .. tags)}))
    end
    table.insert(items, item)
  end
  doc.blocks = {pandoc.BulletList(items)}
  return doc
end
