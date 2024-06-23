
RatingBusterDB = {
	["namespaces"] = {
		["LibDualSpec-1.0"] = {
		},
	},
	["profileKeys"] = {
		{%- for character in account.characters %}
		["{{ character.titled_character_name }} - {{ character.realm_name }}"] = "MyDefault",
		{%- endfor %}
	},
	["profiles"] = {
		["MyDefault"] = {
			["showItemID"] = true,
		},
	},
}
