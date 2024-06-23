
PallyPowerDB = {
	["profiles"] = {
		["MyDefault"] = {
			["freeassign"] = 1,
			["autobuff"] = {
				["autokey1"] = false,
				["autokey2"] = "9",
			},
			["display"] = {
				["frameLocked"] = true,
			},
			["disable"] = false,
		},
		["class/Paladin"] = {
		},
	},
	["currentProfile"] = {
		{%- for character in account.characters %}
		["{{ character.titled_character_name }} - {{ character.realm_name }}"] = "MyDefault",
		{%- endfor %}
	},
}
PallyPower_Assignments = {
	{%- for character in account.characters %}
	["{{ character.titled_character_name }}"] = {
		2, -- [1]
		2, -- [2]
		1, -- [3]
		1, -- [4]
		1, -- [5]
		1, -- [6]
		1, -- [7]
		1, -- [8]
		1, -- [9]
		2, -- [10]
		2, -- [11]
	},
	{%- endfor %}
}
PallyPower_NormalAssignments = {
}
PallyPower_AuraAssignments = {
	{%- for character in account.characters %}
	["{{ character.titled_character_name }}"] = 1,
	{%- endfor %}
}
PallyPower_SavedPresets = {
}
