#!/bin/bash

IFS=' '

# Write header of README
echo "# Pokémon Beryl" > README.md
echo "" >> README.md
echo "A ROM hack of Pokémon Emerald using the [**Pokemon Emerald Decompilation Project**](https://github.com/pret/pokeemerald)." >> README.md
echo "" >> README.md
echo "Currently, the project builds the following ROM:" >> README.md
echo "" >> README.md

# Get sha1sum of game ROM
shasum=$(sha1sum pokeberyl.gba)
read -r -a hash_array <<< "$shasum"

# Write ROM information
echo "**pokeberyl.gba** \`sha1sum: ${hash_array[0]}\`" >> README.md
echo "" >> README.md

# Write installation info
echo "# Installation" >> README.md
echo "Installation instructions can be found in [INSTALL.md](./INSTALL.md)." >> README.md
echo "" >> README.md

# Write legal info
echo "# Legal" >> README.md
echo "This project is not affiliated with or endorsed by Nintendo, Creatures Inc., or any other party connected to the Pokémon franchise." >> README.md
echo "All code is provided as-is without any warranty or guarantees of any kind." >> README.md
