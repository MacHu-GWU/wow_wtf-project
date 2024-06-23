
AtlasLootOptions = nil
AtlasLootDB = {
	["profileKeys"] = {
		{%- for character in account.characters %}
		["{{ character.titled_character_name }} - {{ character.realm_name }}"] = "MyDefault",
		{%- endfor %}
	},
	["profiles"] = {
		["MyDefault"] = {
			["CraftingLink"] = 2,
			["ItemIDs"] = 1,
			["AllLinks"] = false,
			["AtlasLootVersion"] = "51103",
		},
	},
}
AtlasLootWishList = {
	["Options"] = {
	},
	["Shared"] = {
	},
	["Own"] = {
	},
}
