# Factorio Ratio Calculator


## Obtaining Recepies
The console command below will dump all recepies in factorio to ~/Library/Application Support/factorio/script-output/recipes on OSX

```
/c for i, recipa in pairs( game.player.force.recipes ) do local recipadata = { name = recipa.name, category = recipa.category, ingredients = recipa.ingredients, products = recipa.products, energy = recipa.energy } game.write_file( "recipes/"..recipa.name..".txt", serpent.block( recipadata ) ) end
```
