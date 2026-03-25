Debug_Entrance_MapScripts::
	.byte 0

Debug_Entrance_ItemStore::
	lock
	faceplayer
	message gText_HowMayIServeYou
	waitmessage
	pokemart Debug_Entrance_Pokemart_ItemStore
	msgbox gText_PleaseComeAgain, MSGBOX_DEFAULT
	release
	end

	.align 2
Debug_Entrance_Pokemart_ItemStore:
	.2byte ITEM_RUBY
	.2byte ITEM_SAPPHIRE
	.2byte ITEM_EMERALD
	pokemartlistend

Debug_Entrance_GiveSurf::
	lock
	faceplayer
	setflag FLAG_SYS_NATIONAL_DEX
	special EnableNationalPokedex
	setflag FLAG_BADGE05_GET
	giveitem ITEM_HM_SURF
	release
	end
