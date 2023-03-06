req = "https://api-mainnet.magiceden.io/idxv2/getListedNftsByCollectionSymbol?collectionSymbol=entreprenerdz&onChainCollectionAddress=&direction=2&field=1&limit=100&offset=0&mode=all"
# TODO IMPLEMENT CRAWLER... DUH

def get_nfts(amount=100):
    data = {
  "results": [
    {
      "mintAddress": "25Db4g1HKsuCpea8FJrGoKVHqU5AThSFhz3aYYiLVxWD",
      "supply": 1,
      "title": "Entreprenerdz #407",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.08,
      "escrowPubkey": "2umCBtofUVA4ExBjZyXaXF4a9eeMt5Bee83zmWr8d9wd",
      "owner": "3yduPVoK6w2YiASXt5U8YooM5Ty7zQhUiq6mLXbwMVQN",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "4tpoXs3VFdSWHAGcHkXvpyLw2RMXmDWdbrVMhRnPvvFK",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/-HbYSLdTQ43zbZnt9ZsouaeuU9ugoy9lghRoYlq1J_I?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Black Hole"
        },
        {
          "trait_type": "Background",
          "value": "Anime Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Black Jacket"
        },
        {
          "trait_type": "Desk",
          "value": "Gum"
        },
        {
          "trait_type": "Shelf",
          "value": "Wood"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Model Jet"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Earphones"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Light Therapy Lamp"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Suggestive Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Bowl Auburn"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Snow Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Accountant"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/-HbYSLdTQ43zbZnt9ZsouaeuU9ugoy9lghRoYlq1J_I?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T19:56:38.913Z",
      "updatedAt": "2023-03-05T19:56:38.913Z"
    },
    {
      "mintAddress": "BBbmypdEjakr31YBY8mZ8sTEJmexQYuRZK6EyatyirHb",
      "supply": 1,
      "title": "Entreprenerdz #472",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.08,
      "escrowPubkey": "dtgnR7qgG5nBU3tiUVjXxjXh8KxY1YMjadNstCSNeCB",
      "owner": "DoMsqUSqSG3aesBVKjaheQBJSiZT8d91SoZwpUeW7pqB",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "G2ZMeehBkRUaAGPFMqrnyK8ribQYf3MpDw4q7pnkdQW6",
        "expiry": -1
      },
      "id": "8AYeYVY4CeZZeDDeKafTfLEZxQebGo8FCdn2tWYpJrRb",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/hSiT6EOq-47Cqql2guZv0TBvIXD8FSaB0RHZT0tofDQ?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Tropical"
        },
        {
          "trait_type": "Background",
          "value": "Cozy Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "Poindexter"
        },
        {
          "trait_type": "Desk",
          "value": "Gum"
        },
        {
          "trait_type": "Shelf",
          "value": "Lava Core"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Boombox"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Film Camera"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "TV Remote"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Drunk"
        },
        {
          "trait_type": "Hair",
          "value": "Torn Hat"
        },
        {
          "trait_type": "Glasses",
          "value": "Radar Shades"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Compact White"
        },
        {
          "trait_type": "Profession",
          "value": "Entrepreneur"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/hSiT6EOq-47Cqql2guZv0TBvIXD8FSaB0RHZT0tofDQ?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T22:45:39.039Z",
      "updatedAt": "2023-03-05T22:45:39.039Z"
    },
    {
      "mintAddress": "4RaqpLHmTHffcL7iyFDUeAujdawvxTLbH6RXnj7XLYJY",
      "supply": 1,
      "title": "Entreprenerdz #8404",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.08,
      "escrowPubkey": "5UTh2k3LfRuUxbfbDXbskANSew2UpVohNu1d3zUT6swz",
      "owner": "5casZRyiiu2SaAh1fbnVZ8W9kQ5a17q9tG5kp2tdtHcL",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "E227Z7LeHrbXqQTN2hdzjZc4NJGtZjvszxFjL76zTzEZ",
        "expiry": -1
      },
      "id": "DVhPKUXahRoPmfQJhG1kCC5CXznTMEqBbY3mje1wHgkq",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/Bg4373sGsIv-uiPUcKdBd_vUJSK6ymJo5oz76jKb0Ww?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Trash Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Beatz by Nerdz"
        },
        {
          "trait_type": "Desk",
          "value": "Weathered"
        },
        {
          "trait_type": "Shelf",
          "value": "Wood"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Painting"
        },
        {
          "trait_type": "Desk Prop",
          "value": "GigaPower"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Ledger"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Shook"
        },
        {
          "trait_type": "Hair",
          "value": "Bowl Golden"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Snow Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Entrepreneur"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/Bg4373sGsIv-uiPUcKdBd_vUJSK6ymJo5oz76jKb0Ww?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T23:05:03.842Z",
      "updatedAt": "2023-03-05T23:05:03.842Z"
    },
    {
      "mintAddress": "8M878sseVekpKyeGK9YXuSxfmrv66S5WT7bqbA599dJm",
      "supply": 1,
      "title": "Entreprenerdz #4800",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.08,
      "escrowPubkey": "6hLmmjCZHJn7uMNP6CkRc2WBDxGeLm3GBp2JrE351FbL",
      "owner": "ENTRnkpP3erCvcF2nmHzAi41bpjn2LWBoWFAoDnHsk9c",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "2S1iptjxPr76GpNJyjmFM2Abw1h4shSnRcPNTGe9b5P5",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/rhtNnr33VckxDoNqK3yRlwk-k0-QMd3340g8dYib7JE?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Portal"
        },
        {
          "trait_type": "Background",
          "value": "Normie"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "Hitman"
        },
        {
          "trait_type": "Desk",
          "value": "Plum Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Cut Stone"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Hookah"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Fan"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Blowtorch"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Smoking Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Greasy Long"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Wired Black"
        },
        {
          "trait_type": "Profession",
          "value": "Business Developer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/rhtNnr33VckxDoNqK3yRlwk-k0-QMd3340g8dYib7JE?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T23:04:17.843Z",
      "updatedAt": "2023-03-05T23:04:17.843Z"
    },
    {
      "mintAddress": "97xwDoiM6GPfA98bYjYvv1xnJB2s2sx8nwxUgbekqGpS",
      "supply": 1,
      "title": "Entreprenerdz #8753",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.09,
      "escrowPubkey": "H5KQeLXs8rD1jBW45odwiH2EiJupRa1Yg4zX7zGXypPK",
      "owner": "HzVy8JG7D6BrbP26UtUP5oxPNdScyKXrtHBwWkssE9M4",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "53aT9MEZLn2uyKuAPoiv52jKBV8z5KkozT65anTrLKLn",
        "expiry": -1
      },
      "id": "2CoF1zUWmLHdcXmcKJPgoNMder15amnLE3vwrQ5gScqq",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/7jxNvAdXu12eLtA5eHn9X6_-I1GvmEfvVUstaSg8t6A?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Music Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Dark Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Flannel"
        },
        {
          "trait_type": "Desk",
          "value": "Oak"
        },
        {
          "trait_type": "Shelf",
          "value": "Pebble"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Rare Gems"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Microscope"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Moisturiser"
        },
        {
          "trait_type": "Blemish",
          "value": "Acne"
        },
        {
          "trait_type": "Expression",
          "value": "Wicked"
        },
        {
          "trait_type": "Hair",
          "value": "Curtain Golden"
        },
        {
          "trait_type": "Glasses",
          "value": "Prescription"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Tablet"
        },
        {
          "trait_type": "Profession",
          "value": "Marketer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/7jxNvAdXu12eLtA5eHn9X6_-I1GvmEfvVUstaSg8t6A?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T23:05:44.677Z",
      "updatedAt": "2023-03-05T23:05:44.677Z"
    },
    {
      "mintAddress": "B2rdVKgaZ79HaaWkdRk53emrZmHzT6p85wtL6AdBxbv2",
      "supply": 1,
      "title": "Entreprenerdz #3043",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.09,
      "escrowPubkey": "EenADSd2QcAFPLGxLcByAMKygKvAJrUPh3U2wZ8E6yQx",
      "owner": "HzVy8JG7D6BrbP26UtUP5oxPNdScyKXrtHBwWkssE9M4",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "HDZSWBptqtmLFkvmG6TRMAYvnTiiSBpEAZhKTNqT6dSD",
        "expiry": -1
      },
      "id": "ZypXAxTnxPSKXJ22hVBp266jDhPBzGPGqg2nnxw9E2A",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/P7R9tTlQvG9sLWbwtXVpHWnG4JK9orS4BCvhpv-uVTI?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Music Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "Touch Grass"
        },
        {
          "trait_type": "Desk",
          "value": "Oak"
        },
        {
          "trait_type": "Shelf",
          "value": "Scorched"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Open Neon"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Snake"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Blowtorch"
        },
        {
          "trait_type": "Blemish",
          "value": "Scar"
        },
        {
          "trait_type": "Expression",
          "value": "Sheepish"
        },
        {
          "trait_type": "Hair",
          "value": "Curtain Brown"
        },
        {
          "trait_type": "Glasses",
          "value": "Harry"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Wired Black"
        },
        {
          "trait_type": "Profession",
          "value": "Accountant"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/P7R9tTlQvG9sLWbwtXVpHWnG4JK9orS4BCvhpv-uVTI?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T23:05:44.656Z",
      "updatedAt": "2023-03-05T23:05:44.656Z"
    },
    {
      "mintAddress": "EkeSrxDc1LsScabGoTogfhJ6VuJ7HeXRx965tRU15gvX",
      "supply": 1,
      "title": "Entreprenerdz #9823",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.09,
      "escrowPubkey": "7Zksvu6TCprqkvBnba8QHmqMeC1qBUPLLKnmzLtq1UGh",
      "owner": "HzVy8JG7D6BrbP26UtUP5oxPNdScyKXrtHBwWkssE9M4",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "BCUSAzdtyUoK3btEv5QFfJLzifqa7CEULA3AfrWvsfQb",
        "expiry": -1
      },
      "id": "5a2nzhJHhiFxAKDFQ6aEkit543UGzbeozByDJvMay94K",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/1K0_C1cY9m5o6bhaWR-tc6rAyTuTyqohT_oGgI1g_70?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Game Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Fair"
        },
        {
          "trait_type": "Clothes",
          "value": "Boobs"
        },
        {
          "trait_type": "Desk",
          "value": "Cherry Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Pebble"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Stop Sign"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Earphones"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Tesseract"
        },
        {
          "trait_type": "Blemish",
          "value": "Scar"
        },
        {
          "trait_type": "Expression",
          "value": "Delirious"
        },
        {
          "trait_type": "Hair",
          "value": "Curtain Golden"
        },
        {
          "trait_type": "Glasses",
          "value": "Broken Nerd"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Snow Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Marketer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/1K0_C1cY9m5o6bhaWR-tc6rAyTuTyqohT_oGgI1g_70?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T23:05:44.256Z",
      "updatedAt": "2023-03-05T23:05:44.256Z"
    },
    {
      "mintAddress": "FyCoTq8bLGhndsZV9NKLaKFfUsW3wEzzFvLEvivn1cjz",
      "supply": 1,
      "title": "Entreprenerdz #5736",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.091,
      "escrowPubkey": "G71qxaRrfbPHYEg6vPdE8GnFiRGs3g8NtMbjRZdK9RxK",
      "owner": "6p9MtdE6Fau4Q2LrP97WWxrMXMVK9QvsmrVfcMCxuj5D",
      "id": "7DH2HbTWVQwfPgguh7Dq4fwRYJsN6bnndoHi9b6drRYi",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/xWCOvc_RzNy5rHToXv3oU0LwXLUy24snCPSwS_xGsMw?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Game Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Stay Focused"
        },
        {
          "trait_type": "Desk",
          "value": "Weathered"
        },
        {
          "trait_type": "Shelf",
          "value": "Mosaic"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Stop Sign"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Sketchbook"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Rubiks Cube"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Content"
        },
        {
          "trait_type": "Hair",
          "value": "Nerd Middle Part"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Turquoise Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Artist"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/xWCOvc_RzNy5rHToXv3oU0LwXLUy24snCPSwS_xGsMw?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "amm": {
        "poolKey": "AVVymU7mCxW6gb3p9VHB8MVbinLChxVxrheDxuCxeTBz",
        "source": "coral_cube_v2",
        "spotPrice": 1980000000,
        "curveType": "linear",
        "curveDelta": 70000000,
        "lpFeeBp": 200,
        "poolType": "two_sided",
        "nextSpotPrice": 2050000000
      },
      "createdAt": "2023-03-05T20:15:38.384Z",
      "updatedAt": "2023-03-05T20:15:38.384Z"
    },
    {
      "mintAddress": "DfW9ZEaeXJ683XhuK5GCFbE6Te7yqPMyRjFvfbKbBXJg",
      "supply": 1,
      "title": "Entreprenerdz #7379",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.1,
      "escrowPubkey": "z85drYVFi3sixPDJAXV6Mr7mNyuvXyRM5XEzkxzsgGw",
      "owner": "8nmVNHG2xhKLEiwUC5tovA69hmEnUKFFHDsMXiH9eavd",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "5XP22sQr5LA15Hy5eN9AzAtognsK95GpsmfvFiiUbfZf",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/8iah_h7LoqaN9lqLQb8wZSIYEA2WuGbyWZTy54ht_tI?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Music Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Poindexter"
        },
        {
          "trait_type": "Desk",
          "value": "Gum"
        },
        {
          "trait_type": "Shelf",
          "value": "Metal"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Saber Red"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Fan"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Snacks"
        },
        {
          "trait_type": "Blemish",
          "value": "Freckles 1"
        },
        {
          "trait_type": "Expression",
          "value": "Happy"
        },
        {
          "trait_type": "Hair",
          "value": "Dreads"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Wired Black"
        },
        {
          "trait_type": "Profession",
          "value": "Entrepreneur"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/8iah_h7LoqaN9lqLQb8wZSIYEA2WuGbyWZTy54ht_tI?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T19:07:16.112Z",
      "updatedAt": "2023-03-05T19:07:16.112Z"
    },
    {
      "mintAddress": "9PvoWjDXRTL2JUi5E4rMaXquMvwGKS5u6sGW56fNRwCE",
      "supply": 1,
      "title": "Entreprenerdz #291",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.1,
      "escrowPubkey": "85Jps9i8r6rJnEe14LiTLno3P7bcaUCB7PgfUrVgcCj9",
      "owner": "Hx1Juij1mc2NvYsWBj9G8hdnKEw27YrtHtmSuHn8xEkw",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "75ekiXMbN5rkHNuje1P28ESVGAzyWY5z8omCjY33o59E",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/aBdoZ-A9gy5vvBSVeiFRpUaVe0Y7IMUUOc6prIBF_6g?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Suburbs"
        },
        {
          "trait_type": "Background",
          "value": "Penthouse"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "Torn Shirt"
        },
        {
          "trait_type": "Desk",
          "value": "Gum"
        },
        {
          "trait_type": "Shelf",
          "value": "Iron Vein"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Old Electronics"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Smartwatch"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Playman"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Meh Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Curls Black"
        },
        {
          "trait_type": "Glasses",
          "value": "Prescription"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Snow Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Accountant"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/aBdoZ-A9gy5vvBSVeiFRpUaVe0Y7IMUUOc6prIBF_6g?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T20:11:17.140Z",
      "updatedAt": "2023-03-05T20:11:17.140Z"
    },
    {
      "mintAddress": "AvhB9PckhJ4gEXnyUuz4J7NNiS78hwvWfukRfa8QnJy8",
      "supply": 1,
      "title": "Entreprenerdz #720",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.1,
      "escrowPubkey": "9NctDowM4odZ45wBDLRPgFLSoNzgiXp9LvZFLWJpxutT",
      "owner": "GCxFQuGeLHxtxGPHdBxodV5WxkxKVkpsDVaT9dvMk4rS",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "AsKEh9qp13tAeL5EUjZL88wdFmugr8z1HhMJhGZSPVGU",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/_hnEMcAa4iSoAR-ZQ2rvRQQsSYCL9TZLA9NwyD6SsT0?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Tropical"
        },
        {
          "trait_type": "Background",
          "value": "Cozy Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Dark Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Jersey"
        },
        {
          "trait_type": "Desk",
          "value": "Oak"
        },
        {
          "trait_type": "Shelf",
          "value": "Colorful Marble"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Medication"
        },
        {
          "trait_type": "Desk Prop",
          "value": "GMO"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Test Tube"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Suggestive Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Undercut"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Compact Black"
        },
        {
          "trait_type": "Profession",
          "value": "Accountant"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/_hnEMcAa4iSoAR-ZQ2rvRQQsSYCL9TZLA9NwyD6SsT0?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T20:45:23.457Z",
      "updatedAt": "2023-03-05T20:45:23.457Z"
    },
    {
      "mintAddress": "4W9baDyDJdMLLgdifcTp4UQ7F6Q8j9xJQ3wNJ7Ko1Ekk",
      "supply": 1,
      "title": "Entreprenerdz #6423",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.1,
      "escrowPubkey": "284frXkgtQaDpD5eLWddzYvfvRR5FR5GZf6H2kCq4RKg",
      "owner": "AyMDdpjhePFHbb63i2WQdDCBMG5GKkM4pb5xkQ3TbfFi",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "2wfANKri3DStasa8vHFn8Fh9mHcu6iP9kTSTB8eHsAdR",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/Rfrt-MWuTdSnPTjJMUEfgbY2Zw-6Pcfyl71Dd371KqI?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Trash Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Medium"
        },
        {
          "trait_type": "Clothes",
          "value": "Nerd"
        },
        {
          "trait_type": "Desk",
          "value": "Gum"
        },
        {
          "trait_type": "Shelf",
          "value": "Mosaic"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Books"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Fan"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Bong"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Scared Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Curls Black"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Rose Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Marketer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/Rfrt-MWuTdSnPTjJMUEfgbY2Zw-6Pcfyl71Dd371KqI?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T21:00:26.027Z",
      "updatedAt": "2023-03-05T21:00:26.027Z"
    },
    {
      "mintAddress": "5d4w9W2SVasBvQbLLYF1pHjrhzp73RCTE7hNJspnpfXt",
      "supply": 1,
      "title": "Entreprenerdz #3441",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.1,
      "escrowPubkey": "6byhSjbanz46Bo4YWsSnePd9n8GCavFxbLPWWzdS8e9Z",
      "owner": "4uiHeJkpwNriUKfEWYzoLgzCqmGwjNAt4qnGVtnYPEB5",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "EFuqSxrFQL1wkVSkgMQfau79uURw4qVXr3fvxsSTVHdi",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/w1p3EGH9R7hLf0FMUbhBbK-rpTFUHcwfgIwSMNxLrqs?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "City"
        },
        {
          "trait_type": "Background",
          "value": "D&D"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Kimono"
        },
        {
          "trait_type": "Desk",
          "value": "Weathered"
        },
        {
          "trait_type": "Shelf",
          "value": "Ocean Sound"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Books"
        },
        {
          "trait_type": "Desk Prop",
          "value": "DSLR Camera"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Tesseract"
        },
        {
          "trait_type": "Blemish",
          "value": "Scar"
        },
        {
          "trait_type": "Expression",
          "value": "Scared"
        },
        {
          "trait_type": "Hair",
          "value": "Undercut"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "RGB"
        },
        {
          "trait_type": "Profession",
          "value": "Accountant"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/w1p3EGH9R7hLf0FMUbhBbK-rpTFUHcwfgIwSMNxLrqs?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T21:06:17.807Z",
      "updatedAt": "2023-03-05T21:06:17.807Z"
    },
    {
      "mintAddress": "3DLXAmDduEd7x9WcwHcxTnW2A6CTEKZkTvGZiVmvbzSt",
      "supply": 1,
      "title": "Entreprenerdz #4071",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.1,
      "escrowPubkey": "4XncPkF2MDSR5u8bJFZh3B4xp6R8hCxp34Fan7eEdjJ2",
      "owner": "DPWTyyAn6uGJwj1dnBHNiZFJFn1XWQPxNyv7xkWSbczG",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "E57ydTdAURtbWJbN9A3tVfK48ntG8YcUrYUZ1wviK9Ua",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/CB01o5hQh-FYonQOQLrb9-XBF5v3izYhXBLgVYbHhcI?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Crystals"
        },
        {
          "trait_type": "Background",
          "value": "Anime Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Dark Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Vacation"
        },
        {
          "trait_type": "Desk",
          "value": "Plum Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Lava Core"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Rare Gems"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Water Bottle"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Grinder"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Scared Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Boyish Black"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Switch"
        },
        {
          "trait_type": "Profession",
          "value": "Marketer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/CB01o5hQh-FYonQOQLrb9-XBF5v3izYhXBLgVYbHhcI?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T21:54:58.595Z",
      "updatedAt": "2023-03-05T21:54:58.595Z"
    },
    {
      "mintAddress": "44n3MUxLEnCqLaLiy9axoHiWqtCVmo8Ar6mSgEk89kt3",
      "supply": 1,
      "title": "Entreprenerdz #3767",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.149,
      "escrowPubkey": "2nQuup6Ahc3eQg52paQdEEyypJwxx9nc4Vd2Av4qjaFR",
      "owner": "8RdnsNUH7UEHXoabJmvzcpRRpKV4nrBrNGtbjjQNpxHH",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "4kcErAtGeT4noKYHwSfAPAkXoYar5teX6GdsZwMcam59",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/E-gut2xP3SdpqjmPkr59rhJgL0QRnfxwN7oE32amDMo?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Trash Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Torn Cloak"
        },
        {
          "trait_type": "Desk",
          "value": "Cardboard"
        },
        {
          "trait_type": "Shelf",
          "value": "Cut Stone"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Father of Dragons"
        },
        {
          "trait_type": "Desk Prop",
          "value": "GigaPower"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Tesseract"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Satisfied"
        },
        {
          "trait_type": "Hair",
          "value": "Cropped Afro"
        },
        {
          "trait_type": "Glasses",
          "value": "Nerd"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Rose Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Accountant"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/E-gut2xP3SdpqjmPkr59rhJgL0QRnfxwN7oE32amDMo?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T20:07:32.000Z",
      "updatedAt": "2023-03-05T20:07:32.000Z"
    },
    {
      "mintAddress": "2LFCUUMKMvmzxL1kj4v3vAB6hkZRdyUAfkDcoiJsofjK",
      "supply": 1,
      "title": "Entreprenerdz #4324",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.15,
      "escrowPubkey": "FrCvTpdsiX9ovhxjFY5w4AL6F4QUzp5EtQBqjiHDnHMQ",
      "owner": "9ZuQFTrSapQA7vFcokwcUAeTUPhZyHZLp7QqyQLtwvDp",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "6YwYwt4daufC8zB7SjaYyKJCr5Vh6L45VvP1vtN73VHK",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/DSZw3TRGfoB8Cd5ChOGGM_89SpvyMB4a9WNKuOHijX8?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Game Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "Nerd"
        },
        {
          "trait_type": "Desk",
          "value": "Gum"
        },
        {
          "trait_type": "Shelf",
          "value": "Metal"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Model Jet"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Fan"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Playman"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Content"
        },
        {
          "trait_type": "Hair",
          "value": "Boyish Red"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Rose Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Accountant"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/DSZw3TRGfoB8Cd5ChOGGM_89SpvyMB4a9WNKuOHijX8?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T19:25:34.749Z",
      "updatedAt": "2023-03-05T19:25:34.749Z"
    },
    {
      "mintAddress": "C7kbAKiL3RNXL48n2yaGBny71VaTXFvu2j2jLoghozpj",
      "supply": 1,
      "title": "Entreprenerdz #7959",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.15,
      "escrowPubkey": "7L4m8cvmJY7hdQfvEKFD18sdTpvb3FZvwfUqcRicE6wj",
      "owner": "DQZPsKJeiGiuz8qidajEywetfhR6hTEmNHXCgtJZnmRk",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "B3sHR2DkM7hdB82ghP6dLYsTCJiXQnUDgW9mjodzD3N6",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/oKMKWHhA7VASg7v0CSySKVpNE98qjfAK7rjhFe_dO18?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Mom's Basement"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "Health"
        },
        {
          "trait_type": "Desk",
          "value": "Gum"
        },
        {
          "trait_type": "Shelf",
          "value": "Scorched"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Figures"
        },
        {
          "trait_type": "Desk Prop",
          "value": "DSLR Camera"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Tesseract"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Suggestive Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Boyish Black"
        },
        {
          "trait_type": "Glasses",
          "value": "Nerd"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Wired Black"
        },
        {
          "trait_type": "Profession",
          "value": "Business Developer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/oKMKWHhA7VASg7v0CSySKVpNE98qjfAK7rjhFe_dO18?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T22:51:44.007Z",
      "updatedAt": "2023-03-05T22:51:44.007Z"
    },
    {
      "mintAddress": "3Roe9ZrzKDcMd42B12wHn1Y64XK7KbcH8u827xD6mZKF",
      "supply": 1,
      "title": "Entreprenerdz #3843",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.1528,
      "escrowPubkey": "88k5PJkZHp2aBAcvGrHhrygGni3UpMMMFUevQeKeryEL",
      "owner": "perce3N2p5LSHcKS8AUpzqgogvNaiQc1zMapfuKRdBx",
      "id": "7WAReeQJsnXLk4LaraoXNb8q2mmxAfpih6NZLCxtpYDR",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/5EJWT-_FYogL2brf3LVbyTdA53flo1wekx8zObT0IbY?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Game Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Torn Cloak"
        },
        {
          "trait_type": "Desk",
          "value": "Oak"
        },
        {
          "trait_type": "Shelf",
          "value": "Wood"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Scythe"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Calculator"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Frog Incense"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Satisfied"
        },
        {
          "trait_type": "Hair",
          "value": "Curls Black"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Compact White"
        },
        {
          "trait_type": "Profession",
          "value": "Accountant"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/5EJWT-_FYogL2brf3LVbyTdA53flo1wekx8zObT0IbY?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "amm": {
        "poolKey": "2iEvHywd5pvtcnDmHrZh6wQELhbBZHrGZ6456aWempPU",
        "source": "coral_cube_v2",
        "spotPrice": 2000000000,
        "curveType": "linear",
        "curveDelta": 70000000,
        "lpFeeBp": 400,
        "poolType": "two_sided",
        "nextSpotPrice": 2070000000
      },
      "createdAt": "2023-03-05T16:47:24.909Z",
      "updatedAt": "2023-03-05T16:47:24.909Z"
    },
    {
      "mintAddress": "HAqff4p4iLUfPF7nm3CFZNa93FXtgdbFTWyDokK9sNKq",
      "supply": 1,
      "title": "Entreprenerdz #5795",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.1624,
      "escrowPubkey": "5FBB8QTgcsgA6x6ymqGkC3ZQxW5kMMGfmxGS4xL3oVgt",
      "owner": "6p9MtdE6Fau4Q2LrP97WWxrMXMVK9QvsmrVfcMCxuj5D",
      "id": "2GJDQZpgdUYmjAUHMeHAUKFpiHcJH9AHMyM8kvXWCHh1",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/nrohcFpmh4KOcW_lSOOZaytVaE_yDTLnSMczcgkSIbc?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Tropical"
        },
        {
          "trait_type": "Background",
          "value": "Dungeon"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Medium"
        },
        {
          "trait_type": "Clothes",
          "value": "Giga Polo"
        },
        {
          "trait_type": "Desk",
          "value": "Cherry Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Wood"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Saber Red"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Giga Mecha"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Frog Incense"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Scared"
        },
        {
          "trait_type": "Hair",
          "value": "Torn Hat"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Turquoise Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Entrepreneur"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/nrohcFpmh4KOcW_lSOOZaytVaE_yDTLnSMczcgkSIbc?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "amm": {
        "poolKey": "AVVymU7mCxW6gb3p9VHB8MVbinLChxVxrheDxuCxeTBz",
        "source": "coral_cube_v2",
        "spotPrice": 1980000000,
        "curveType": "linear",
        "curveDelta": 70000000,
        "lpFeeBp": 200,
        "poolType": "two_sided",
        "nextSpotPrice": 2120000000,
        "mmmPoolRank": 1
      },
      "createdAt": "2023-03-05T19:18:44.545Z",
      "updatedAt": "2023-03-05T19:18:44.545Z"
    },
    {
      "mintAddress": "GgZtU6x9rJqGUiJbAqxVuPhjDtikx4N1n1aL3S6GTmXv",
      "supply": 1,
      "title": "Entreprenerdz #2337",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.17999999902,
      "escrowPubkey": "VYDYQ8ptVai7NFnda6PLPbAMt6tDJBEeTtn75KuzU5A",
      "owner": "HiH4fkQSXfrtU9tVv7boG2QDMxVw5yi9M56L7VqL8vBD",
      "id": "976qh8w6N8ZXMGDDCAhEGr1euW5yE4i2sCeYyTXE5d8b",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/De2YI6QUWsM-ImnyMJCEYxJ07l9RnAUk9PPviOf6pG8?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Trash Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "Lab Coat"
        },
        {
          "trait_type": "Desk",
          "value": "Oak"
        },
        {
          "trait_type": "Shelf",
          "value": "Scorched"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Ouija Board"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Water Bottle"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "TV Remote"
        },
        {
          "trait_type": "Blemish",
          "value": "Freckles 1"
        },
        {
          "trait_type": "Expression",
          "value": "Content"
        },
        {
          "trait_type": "Hair",
          "value": "Dreads"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Turntables"
        },
        {
          "trait_type": "Profession",
          "value": "Business Developer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/De2YI6QUWsM-ImnyMJCEYxJ07l9RnAUk9PPviOf6pG8?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "amm": {
        "poolKey": "36WHyK24d2WwLBTiXX4KPL4ueXkNjHgmfpDEpBn8Pdig",
        "source": "coral_cube_v2",
        "spotPrice": 2137254901,
        "curveType": "exp",
        "curveDelta": 200,
        "lpFeeBp": 400,
        "poolType": "sell_sided",
        "nextSpotPrice": 2179999999.02
      },
      "createdAt": "2023-03-05T18:36:20.694Z",
      "updatedAt": "2023-03-05T18:36:20.694Z"
    },
    {
      "mintAddress": "HrWpah5ziCQAhVAHegziRKA9FNHn9KnMiNMYUrAdsD2P",
      "supply": 1,
      "title": "Entreprenerdz #4050",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.18,
      "escrowPubkey": "6uUPPp3H5W7LUmz3u72rqhtHobUtyRRVR9vPxWJeNjVW",
      "owner": "9kGkhqxszxbZ6qiwoRVXRTyxsSiahbdTyo9ude1xsRjp",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "4wd5dzXdUAHojZuMQJ1ziKYm8TG1gyoV4T55wcrEBDeG",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/l_y2jv-lHRvEH3u8U-jGDMIITwSJiUULSxPX3OKp_s8?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Suburbs"
        },
        {
          "trait_type": "Background",
          "value": "Cozy Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Beatz by Nerdz"
        },
        {
          "trait_type": "Desk",
          "value": "Plum Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Iron Vein"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Bachelor Pad"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Coffee Spill"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Ledger"
        },
        {
          "trait_type": "Blemish",
          "value": "Freckles 1"
        },
        {
          "trait_type": "Expression",
          "value": "WTF"
        },
        {
          "trait_type": "Hair",
          "value": "Boyish Black"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Classic White"
        },
        {
          "trait_type": "Profession",
          "value": "Accountant"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/l_y2jv-lHRvEH3u8U-jGDMIITwSJiUULSxPX3OKp_s8?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T18:31:27.900Z",
      "updatedAt": "2023-03-05T18:31:27.900Z"
    },
    {
      "mintAddress": "AMryLdbAz3QMXss8Erj7hN4i5Mzqj7BBBnKZKqV3v3wi",
      "supply": 1,
      "title": "Entreprenerdz #9075",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.18,
      "escrowPubkey": "Au8KcUYBZNYHSVz1UsNzVvPUztbXfguRk2VrJiNQkzCs",
      "owner": "8nmVNHG2xhKLEiwUC5tovA69hmEnUKFFHDsMXiH9eavd",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "Do9qeYF2t3wwp6GCPjjeTyhKqEagNMvQVFriJ4NeLsQJ",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/fBkaAVsfQDDUdCtGfv3E846j3rRiumMplYbbB5BIzG4?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "City"
        },
        {
          "trait_type": "Background",
          "value": "Trader Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Dark Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Flannel"
        },
        {
          "trait_type": "Desk",
          "value": "Cherry Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Mosaic"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Father of Dragons"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Journal"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Ledger"
        },
        {
          "trait_type": "Blemish",
          "value": "Acne"
        },
        {
          "trait_type": "Expression",
          "value": "Satisfied"
        },
        {
          "trait_type": "Hair",
          "value": "Boyish Red"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Turquoise Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Marketer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/fBkaAVsfQDDUdCtGfv3E846j3rRiumMplYbbB5BIzG4?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T18:30:13.366Z",
      "updatedAt": "2023-03-05T18:30:13.366Z"
    },
    {
      "mintAddress": "8UF8LPZCsyXxZSDtG514RxCjJdtG9GvpZ5ZVFDvToPcX",
      "supply": 1,
      "title": "Entreprenerdz #8744",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.18,
      "escrowPubkey": "ECQAKEN9sXpCNwUNjjhFwAMxER4vxs6ME8CdEhh3YkAR",
      "owner": "8nmVNHG2xhKLEiwUC5tovA69hmEnUKFFHDsMXiH9eavd",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "FsV1cNSJWis25xnFsHFRRed4mNjcws6XeuUyQ9136yAd",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/bn-SNaHP283KelcSzYD03FywjPfaNU-SdlAem9cNp_Y?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Suburbs"
        },
        {
          "trait_type": "Background",
          "value": "Degenformers"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Denim Jacket"
        },
        {
          "trait_type": "Desk",
          "value": "Cardboard"
        },
        {
          "trait_type": "Shelf",
          "value": "Mosaic"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Ship in a Bottle"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Floating Moon"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Glass"
        },
        {
          "trait_type": "Blemish",
          "value": "Freckles 2"
        },
        {
          "trait_type": "Expression",
          "value": "Scared Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Rock N' Roll Golden"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "RGB"
        },
        {
          "trait_type": "Profession",
          "value": "Business Developer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/bn-SNaHP283KelcSzYD03FywjPfaNU-SdlAem9cNp_Y?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T18:30:13.374Z",
      "updatedAt": "2023-03-05T18:30:13.374Z"
    },
    {
      "mintAddress": "3JvDZKh3qeiCoyiKv6qhYqCKvbTMxHN1eLmKmj7FNVaH",
      "supply": 1,
      "title": "Entreprenerdz #2191",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.2,
      "escrowPubkey": "8EcrAX4HBEA7uxFe4GBQkwkiNzj4A4pcKVsfUdK4s7Es",
      "owner": "HzxrbZwPWjPidRFUTkUP9P9zoX6gwvZLk8XhmfmQtuaD",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "6Zp8UYT6CWzsSyrzHf578rFWQwurj9wucSwUdLdVw3n9",
        "expiry": -1
      },
      "id": "GqbcaYFb5Lp77zmnk4ucf1KZMwyZjhzBkLAAUPMuRiXm",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/wqoYI3HmQesuOthgX4S4V6RpA6KRab2Xk6jBdsdnSkQ?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Suburbs"
        },
        {
          "trait_type": "Background",
          "value": "Anime Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "Boxing Robe"
        },
        {
          "trait_type": "Desk",
          "value": "Weathered"
        },
        {
          "trait_type": "Shelf",
          "value": "Metal"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Old Electronics"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Microscope"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Newton's Cradle Pendulum"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Drunk Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Torn Hat"
        },
        {
          "trait_type": "Glasses",
          "value": "Radar Shades"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Snow Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Business Developer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/wqoYI3HmQesuOthgX4S4V6RpA6KRab2Xk6jBdsdnSkQ?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T18:49:46.279Z",
      "updatedAt": "2023-03-05T18:49:46.279Z"
    },
    {
      "mintAddress": "Er5ggLvZCjboroMeJ7SRi5Y3E5kySMLqBAQDXfyadzUC",
      "supply": 1,
      "title": "Entreprenerdz #689",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.2,
      "escrowPubkey": "8ouLohN7ZQj1bf1bbxHiAGieycFkY3LfMDNDg4QJPjsK",
      "owner": "7CKtdQfwr6HRuyjxzzxnfNiyfC89vJxVgiE2f3m65Dva",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "B5GW5JnF87n3hGXyvsAqdbivvfBDP4xrTMjJUQpy3TGm",
        "expiry": -1
      },
      "id": "DizYGGpRDYDrf19C2Y83UxAoFJEC8P4wfzFnF7CaeLij",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/Y5YaxPsTLGB7mcwB1aZ4yLzPU_K-3utPAv9uQrWc4AE?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Game Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "Lab Coat"
        },
        {
          "trait_type": "Desk",
          "value": "Weathered"
        },
        {
          "trait_type": "Shelf",
          "value": "Wood"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Morpheus"
        },
        {
          "trait_type": "Desk Prop",
          "value": "VR Controllers"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Wallet & Keys"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Shook"
        },
        {
          "trait_type": "Hair",
          "value": "Boyish Red"
        },
        {
          "trait_type": "Glasses",
          "value": "Broken Nerd"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "RGB"
        },
        {
          "trait_type": "Profession",
          "value": "Marketer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/Y5YaxPsTLGB7mcwB1aZ4yLzPU_K-3utPAv9uQrWc4AE?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T20:35:18.605Z",
      "updatedAt": "2023-03-05T20:35:18.605Z"
    },
    {
      "mintAddress": "Htv4v2waAt7LstMpVJuNEb78beCw5CYVtpWRwwzZfEMF",
      "supply": 1,
      "title": "Entreprenerdz #9443",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.2161419989294,
      "escrowPubkey": "3xmCAgjKxb9AmBTy1HRBb5jGDoPbWVffo37hhVbUkm57",
      "owner": "DKVJeggxTCcuZCGsRF4aWR28awzXkDwDq17wtTemAdAb",
      "id": "9bcm29yZir6xzSyDEEcGfCUfYBPR5y9dr3T9t6mD5BEi",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/L3ql0ah23d92v5g6VYrYd67MgLWRQ0UduhJu07IsRw0?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Game Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Lab Coat"
        },
        {
          "trait_type": "Desk",
          "value": "Cherry Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Mosaic"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Scythe"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Smartwatch"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Dice"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Wicked"
        },
        {
          "trait_type": "Hair",
          "value": "Curtain Brown"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Classic White"
        },
        {
          "trait_type": "Profession",
          "value": "Entrepreneur"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/L3ql0ah23d92v5g6VYrYd67MgLWRQ0UduhJu07IsRw0?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "amm": {
        "poolKey": "EGfQVMKJH9rjKbKa4AWfsn4sGvToJm1xqndZk27nrKA",
        "source": "coral_cube_v2",
        "spotPrice": 2069999999,
        "curveType": "exp",
        "curveDelta": 100,
        "lpFeeBp": 600,
        "poolType": "two_sided",
        "nextSpotPrice": 2090699998.99
      },
      "createdAt": "2023-03-05T17:40:56.712Z",
      "updatedAt": "2023-03-05T17:40:56.712Z"
    },
    {
      "mintAddress": "8nvWu4AnuJGeEagN61WdniJ3AGjpscn6oSvaVBXd2zPV",
      "supply": 1,
      "title": "Entreprenerdz #8852",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.223599999,
      "escrowPubkey": "Ab8YCJ5o6R6X5yH7u7v1qWrnrawLKGSRVWaodXvpRU41",
      "owner": "HiH4fkQSXfrtU9tVv7boG2QDMxVw5yi9M56L7VqL8vBD",
      "id": "G8RW2w1mSerNHm8yPrXXxeauVNj5HMK4XKKGoCiVUYe3",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/oljYnxsZ5SyTrvheHUggCQUUqjkBLL8NsjK4wYuYRxU?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Music Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Fair"
        },
        {
          "trait_type": "Clothes",
          "value": "Nerd"
        },
        {
          "trait_type": "Desk",
          "value": "Gum"
        },
        {
          "trait_type": "Shelf",
          "value": "Scorched"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Pyramid"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Water Bottle"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Light Therapy Lamp"
        },
        {
          "trait_type": "Blemish",
          "value": "Acne"
        },
        {
          "trait_type": "Expression",
          "value": "Suggestive Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Brown Fox"
        },
        {
          "trait_type": "Glasses",
          "value": "Classic Shades"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Compact Black"
        },
        {
          "trait_type": "Profession",
          "value": "Artist"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/oljYnxsZ5SyTrvheHUggCQUUqjkBLL8NsjK4wYuYRxU?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "amm": {
        "poolKey": "36WHyK24d2WwLBTiXX4KPL4ueXkNjHgmfpDEpBn8Pdig",
        "source": "coral_cube_v2",
        "spotPrice": 2137254901,
        "curveType": "exp",
        "curveDelta": 200,
        "lpFeeBp": 400,
        "poolType": "sell_sided",
        "nextSpotPrice": 2223599999.0004,
        "mmmPoolRank": 1
      },
      "createdAt": "2023-03-05T17:46:06.860Z",
      "updatedAt": "2023-03-05T17:46:06.860Z"
    },
    {
      "mintAddress": "85vEmj8mzLJZJsy4wVgdKNkmwiJuAWkoUjoFQDejGGgf",
      "supply": 1,
      "title": "Entreprenerdz #4879",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.2256,
      "escrowPubkey": "25pXjxVumYc9EzQYtUMbvniGzNfSoWff72f9sun9wX6m",
      "owner": "perce3N2p5LSHcKS8AUpzqgogvNaiQc1zMapfuKRdBx",
      "id": "9SLhWfuu7o8Qp8x6YterAiPZSw4JCZCvyBgaGvEQgahs",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/MYPRErJvvD1HD2Hc-PRQQCp2FNhYyYV5iyu3Whydgc0?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Game Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Fair"
        },
        {
          "trait_type": "Clothes",
          "value": "Leather Jacket"
        },
        {
          "trait_type": "Desk",
          "value": "Cardboard"
        },
        {
          "trait_type": "Shelf",
          "value": "Galaxy"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Sparky"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Earphones"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Grinder"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Suggestive Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Messy"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Compact Black"
        },
        {
          "trait_type": "Profession",
          "value": "Entrepreneur"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/MYPRErJvvD1HD2Hc-PRQQCp2FNhYyYV5iyu3Whydgc0?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "amm": {
        "poolKey": "2iEvHywd5pvtcnDmHrZh6wQELhbBZHrGZ6456aWempPU",
        "source": "coral_cube_v2",
        "spotPrice": 2000000000,
        "curveType": "linear",
        "curveDelta": 70000000,
        "lpFeeBp": 400,
        "poolType": "two_sided",
        "nextSpotPrice": 2140000000,
        "mmmPoolRank": 1
      },
      "createdAt": "2023-03-05T19:14:40.183Z",
      "updatedAt": "2023-03-05T19:14:40.183Z"
    },
    {
      "mintAddress": "FHUEyFsbNgonzQkr3uBTcv5YeUggdHV7tsWrzwb8UyJQ",
      "supply": 1,
      "title": "Entreprenerdz #3577",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.23,
      "escrowPubkey": "Ab87q77AaFxcJ4BFuh1sWVnYBt98SFqZGPkvP9mDzkhn",
      "owner": "Hmp55fuqynBpfFkiYxVkSA8sWz9TS61H17sfAGexWce6",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "Xc6NE6Fz5kgkacAr9g76LTszGUT8UDX3qzVj7S4KrJz",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/I8EdCrNoep3B74e_BsME_--N2N_OV6V5OynyBKROK6o?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Suburbs"
        },
        {
          "trait_type": "Background",
          "value": "D&D"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Fair"
        },
        {
          "trait_type": "Clothes",
          "value": "Overalls"
        },
        {
          "trait_type": "Desk",
          "value": "Oak"
        },
        {
          "trait_type": "Shelf",
          "value": "Cut Stone"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Boombox"
        },
        {
          "trait_type": "Desk Prop",
          "value": "GMO"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Newton's Cradle Pendulum"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Crazy"
        },
        {
          "trait_type": "Hair",
          "value": "Dreads"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Classic White"
        },
        {
          "trait_type": "Profession",
          "value": "Accountant"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/I8EdCrNoep3B74e_BsME_--N2N_OV6V5OynyBKROK6o?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T18:13:43.176Z",
      "updatedAt": "2023-03-05T18:13:43.176Z"
    },
    {
      "mintAddress": "BGJoYzPW7CpyEgNCdsWvdrMd3uVu7PwcRFPgFhimRLi3",
      "supply": 1,
      "title": "Entreprenerdz #6658",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.232323232,
      "escrowPubkey": "6MRDNH8ZxezULGfjpjWK3oKhWQfNVXdwnSsbCgfR4nGr",
      "owner": "hadeaC5JQvAJugvsa97BPPSdeGQzhWxqK6DAqq5TsW8",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "4UouCRM1AU4uVgKp4xhirokWKPAWTwumRKCxEpENXNfB",
        "expiry": -1
      },
      "id": "EdqU3ki3Sc1fHJ7vE28FgSUcEcUYBPT926UxWNdThQxW",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/WcIt0L2zhLcnm3vAZtnSP1WWefN9f6aK8atGOaf-70w?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Suburbs"
        },
        {
          "trait_type": "Background",
          "value": "Cozy Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "Flannel"
        },
        {
          "trait_type": "Desk",
          "value": "Cardboard"
        },
        {
          "trait_type": "Shelf",
          "value": "Malachite"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Open Neon"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Water Bottle"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Wallet & Keys"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Smoking Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Curtain Brown"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Classic White"
        },
        {
          "trait_type": "Profession",
          "value": "Artist"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/WcIt0L2zhLcnm3vAZtnSP1WWefN9f6aK8atGOaf-70w?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T19:15:30.048Z",
      "updatedAt": "2023-03-05T19:15:30.048Z"
    },
    {
      "mintAddress": "3beo9bws4aECoFnuf8oMAE7KQ2eynj6cfCNUFjW46HUz",
      "supply": 1,
      "title": "Entreprenerdz #6301",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.2338,
      "escrowPubkey": "BVQseEYfjECrUMpzW9fqTZPbwHYEGkNogJv6UuxKXwSN",
      "owner": "6p9MtdE6Fau4Q2LrP97WWxrMXMVK9QvsmrVfcMCxuj5D",
      "id": "B9855XcXHrf4SA6MAtCkxFNmKusNJFJeLam6jZ36Cho7",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/JyEb623XoXDrBJzFVvZsJrbl5XQnQTaw9oBgGZNrdzg?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Black Hole"
        },
        {
          "trait_type": "Background",
          "value": "Normie"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Flannel"
        },
        {
          "trait_type": "Desk",
          "value": "Oak"
        },
        {
          "trait_type": "Shelf",
          "value": "Mosaic"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Books"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Earphones"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Blowtorch"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Meh Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Dreads"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Switch"
        },
        {
          "trait_type": "Profession",
          "value": "Entrepreneur"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/JyEb623XoXDrBJzFVvZsJrbl5XQnQTaw9oBgGZNrdzg?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "amm": {
        "poolKey": "AVVymU7mCxW6gb3p9VHB8MVbinLChxVxrheDxuCxeTBz",
        "source": "coral_cube_v2",
        "spotPrice": 1980000000,
        "curveType": "linear",
        "curveDelta": 70000000,
        "lpFeeBp": 200,
        "poolType": "two_sided",
        "nextSpotPrice": 2190000000,
        "mmmPoolRank": 2
      },
      "createdAt": "2023-03-05T18:28:56.354Z",
      "updatedAt": "2023-03-05T18:28:56.354Z"
    },
    {
      "mintAddress": "ytDHPt7ASPmQLuu4Lm9YVpFikTy6pmuoaCJSjGbm762",
      "supply": 1,
      "title": "Entreprenerdz #801",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.238303418,
      "escrowPubkey": "2ipt9e3VjhYyRAKLi9A3p6DGLVGdVKUScsT6PomWPgTf",
      "owner": "DKVJeggxTCcuZCGsRF4aWR28awzXkDwDq17wtTemAdAb",
      "id": "Hvkyb4tnjfgnMymyXLwvDK8cqjaZZjqmhyhapxvUKD9Q",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/GeqggoXlhMOLJom5lG_US1_BQjlLUxv1qk6cVuQaE8c?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Space"
        },
        {
          "trait_type": "Background",
          "value": "Normie"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Jersey"
        },
        {
          "trait_type": "Desk",
          "value": "Weathered"
        },
        {
          "trait_type": "Shelf",
          "value": "Wood"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Pyramid"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Coffee Spill"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Drinking Bird"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Wicked"
        },
        {
          "trait_type": "Hair",
          "value": "Curtain Black"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Compact Black"
        },
        {
          "trait_type": "Profession",
          "value": "Artist"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/GeqggoXlhMOLJom5lG_US1_BQjlLUxv1qk6cVuQaE8c?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "amm": {
        "poolKey": "EGfQVMKJH9rjKbKa4AWfsn4sGvToJm1xqndZk27nrKA",
        "source": "coral_cube_v2",
        "spotPrice": 2069999999,
        "curveType": "exp",
        "curveDelta": 100,
        "lpFeeBp": 600,
        "poolType": "two_sided",
        "nextSpotPrice": 2111606998.9799,
        "mmmPoolRank": 1
      },
      "createdAt": "2023-03-05T18:03:02.414Z",
      "updatedAt": "2023-03-05T18:03:02.414Z"
    },
    {
      "mintAddress": "FnKeR863hUeskfRG24ykYsHEWzny1fauid65QQnMyqkP",
      "supply": 1,
      "title": "Entreprenerdz #4182",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.24,
      "escrowPubkey": "FZ3N4KkmivNHYkzBczCTSFxMbnNRvpoy6niPw9tKXzFZ",
      "owner": "EnHCgmi6noHQVkeKotNGnqiy3pFmCTu6zhtA2H949Hgm",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "4g4PQY7XW7WueUHfKzwpn9sqTmW7rSZ1bSH773GeYukH",
        "expiry": -1
      },
      "id": "8sWNkijc7ZFHvSxJfDGFCzYAGhZ5mywWDAAkrbtPjeku",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/GPyUSO2z6fO530ALcgybX9IKxqvsodke_YkLz1ropic?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Tropical"
        },
        {
          "trait_type": "Background",
          "value": "Trader Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Beatz by Nerdz"
        },
        {
          "trait_type": "Desk",
          "value": "Plum Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Metal"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Troop"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Megaman"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Snacks"
        },
        {
          "trait_type": "Blemish",
          "value": "Freckles 2"
        },
        {
          "trait_type": "Expression",
          "value": "Happy Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Bowl Auburn"
        },
        {
          "trait_type": "Glasses",
          "value": "Broken Nerd"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Turquoise Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Degen"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/GPyUSO2z6fO530ALcgybX9IKxqvsodke_YkLz1ropic?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T22:53:47.144Z",
      "updatedAt": "2023-03-05T22:53:47.144Z"
    },
    {
      "mintAddress": "3jFZWzTfDtrjziPsuDnYTNUWTLPACHTANFrhR5XvGYW4",
      "supply": 1,
      "title": "Entreprenerdz #2162",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.242424242,
      "escrowPubkey": "B68oR8Jg8kPt8i5uNXU1FhzR4xLqFXvJp5p7J3ceNWxr",
      "owner": "hadeaC5JQvAJugvsa97BPPSdeGQzhWxqK6DAqq5TsW8",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "EFAJRfFRV1RV4xPSmxNsKj3fZeDRGqqjWLme11Ju8SWq",
        "expiry": -1
      },
      "id": "CNiK32Lpdvc37xL4qbsnTLrHqidgSfvRhXhjmXoXsJM",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/cmnnMwwBXXVjxsrIoKzkVwHUXfg8JdVq0Cxk5fU2hFc?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Mom's Basement"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "Black Jacket"
        },
        {
          "trait_type": "Desk",
          "value": "Plum Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Pebble"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Record Player"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Journal"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Glass"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Sheepish"
        },
        {
          "trait_type": "Hair",
          "value": "Bald"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Switch"
        },
        {
          "trait_type": "Profession",
          "value": "Artist"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/cmnnMwwBXXVjxsrIoKzkVwHUXfg8JdVq0Cxk5fU2hFc?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T19:15:29.112Z",
      "updatedAt": "2023-03-05T19:15:29.112Z"
    },
    {
      "mintAddress": "C91ruMibbhXRGs2MNxtBeQ733H8Mxg3bpjEbNPhDVSur",
      "supply": 1,
      "title": "Entreprenerdz #6598",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.25,
      "escrowPubkey": "CtKaTZAT5RR9aVX1TTvKSDPx7UfZBFxLbEE6J33BXrQo",
      "owner": "7q6vYUzzHPUFH7FnnuxB4jCS9JE7dNJXaipoUjAWPGHm",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "D5D7fn3RF6pJW7zH9UB1eJAbE9Qa8zeqfXsWG2GbCiS8",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/Wn7r85tJEz192P2gt7NzUfFGyv6JtGQkiD4OKbB5lPs?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Music Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "Stay Focused"
        },
        {
          "trait_type": "Desk",
          "value": "Plum Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Metal"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Saber Red"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Smartwatch"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Vape"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "WTF"
        },
        {
          "trait_type": "Hair",
          "value": "Boyish Red"
        },
        {
          "trait_type": "Glasses",
          "value": "Radar Shades"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Compact White"
        },
        {
          "trait_type": "Profession",
          "value": "Degen"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/Wn7r85tJEz192P2gt7NzUfFGyv6JtGQkiD4OKbB5lPs?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T20:13:18.844Z",
      "updatedAt": "2023-03-05T20:13:18.844Z"
    },
    {
      "mintAddress": "dfPHggTuSVEXmATspNdCoYWE5hQygLoRuBTLNuwAD4D",
      "supply": 1,
      "title": "Entreprenerdz #1740",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.25,
      "escrowPubkey": "DsjizNWTUGKyt2rYRsDNo7aYKKcD7aKdmouba3ouT4SR",
      "owner": "7q6vYUzzHPUFH7FnnuxB4jCS9JE7dNJXaipoUjAWPGHm",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "79asSfLahenGQyk4CD7nHdTrgjWRaX65QRaGwDekMuok",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/Izm3Fym39b2Zuf4w6RVOGhgEo_UevqwjCpK1sdXqAIw?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Trash Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Stay Focused"
        },
        {
          "trait_type": "Desk",
          "value": "Metal"
        },
        {
          "trait_type": "Shelf",
          "value": "Wood"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Boombox"
        },
        {
          "trait_type": "Desk Prop",
          "value": "VR Controllers"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Space Shuttle"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Suggestive"
        },
        {
          "trait_type": "Hair",
          "value": "Torn Hat"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Turntables"
        },
        {
          "trait_type": "Profession",
          "value": "Marketer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/Izm3Fym39b2Zuf4w6RVOGhgEo_UevqwjCpK1sdXqAIw?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T20:13:18.622Z",
      "updatedAt": "2023-03-05T20:13:18.622Z"
    },
    {
      "mintAddress": "H3QX45AEip67jd74UyHYh3en5bVK9SaUWvKVDpAZ27Ub",
      "supply": 1,
      "title": "Entreprenerdz #7618",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.25,
      "escrowPubkey": "9iGfYyZjPcQhTaQG6iMJWPLAf4Hf5kstKuDgGEb81m5B",
      "owner": "7q6vYUzzHPUFH7FnnuxB4jCS9JE7dNJXaipoUjAWPGHm",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "LHRctiW8qLrnvAksswoVjxvFqs2GyAq9t66ukrMz9cW",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/JgrYyvtvr1ijtAcFEQ29U0ixeScE7QflE0-lY3Mp5fg?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Suburbs"
        },
        {
          "trait_type": "Background",
          "value": "Cozy Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Denim Jacket"
        },
        {
          "trait_type": "Desk",
          "value": "Cherry Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Galaxy"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Stop Sign"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Microscope"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Newton's Cradle Pendulum"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "WTF"
        },
        {
          "trait_type": "Hair",
          "value": "Curtain Black"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Switch"
        },
        {
          "trait_type": "Profession",
          "value": "Marketer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/JgrYyvtvr1ijtAcFEQ29U0ixeScE7QflE0-lY3Mp5fg?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T20:13:19.091Z",
      "updatedAt": "2023-03-05T20:13:19.091Z"
    },
    {
      "mintAddress": "5wzBje3nCKPezF3sLRTqDsHhZr5MbaSyUWFKdyHJxCDc",
      "supply": 1,
      "title": "Entreprenerdz #4580",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.25,
      "escrowPubkey": "Du9rsSL8JXJejmrffXoN8XoNQ1nT6wDF9NDHjtyyEPpx",
      "owner": "7q6vYUzzHPUFH7FnnuxB4jCS9JE7dNJXaipoUjAWPGHm",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "AuNHgp4ShSaDNTC2aEbrbYjVM4qQ8JrbeuDwTBPqJUuZ",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/6iHUaUnHX4B_amG5VuQfaBmZgS1mXSgurCiyi51y9TA?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "City"
        },
        {
          "trait_type": "Background",
          "value": "D&D"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Fair"
        },
        {
          "trait_type": "Clothes",
          "value": "Agent S"
        },
        {
          "trait_type": "Desk",
          "value": "Plum Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Pebble"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Old Electronics"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Fan"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Drinking Bird"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Angry"
        },
        {
          "trait_type": "Hair",
          "value": "Cropped Afro"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Snow Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Entrepreneur"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/6iHUaUnHX4B_amG5VuQfaBmZgS1mXSgurCiyi51y9TA?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T20:13:18.255Z",
      "updatedAt": "2023-03-05T20:13:18.255Z"
    },
    {
      "mintAddress": "CugUG4RNVtd8Wk4GrSm4ssr4ZSdFLtMisW7YxyLBWyDD",
      "supply": 1,
      "title": "Entreprenerdz #841",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.25,
      "escrowPubkey": "YVGaSqsZiHCFggWhf3A8xCBN8qjrZfDXgFtUDNrwL9i",
      "owner": "7q6vYUzzHPUFH7FnnuxB4jCS9JE7dNJXaipoUjAWPGHm",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "BhfWQnmxLSj83UHW7WMQ7X4sUHftzsjEY6T636vzZkB",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/e6pGrVDephd6xw39hQpBQDIXBdJ_0XtZg3zd4hT7syI?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Black Hole"
        },
        {
          "trait_type": "Background",
          "value": "Penthouse"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "Poindexter"
        },
        {
          "trait_type": "Desk",
          "value": "Cherry Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Lava Core"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Boombox"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Sketchbook"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Wallet & Keys"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Shook"
        },
        {
          "trait_type": "Hair",
          "value": "Messy"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "RGB"
        },
        {
          "trait_type": "Profession",
          "value": "Degen"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/e6pGrVDephd6xw39hQpBQDIXBdJ_0XtZg3zd4hT7syI?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T20:13:18.968Z",
      "updatedAt": "2023-03-05T20:13:18.968Z"
    },
    {
      "mintAddress": "GjpfugNgYPU51MwL5tMCsxNG1vTFg9j4B7YLzbBstkAs",
      "supply": 1,
      "title": "Entreprenerdz #1545",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.25,
      "escrowPubkey": "7iJ7YBFZLYobTAgbwq6ZQzJpnuy9bKG2DfwfUuuhc3UP",
      "owner": "7q6vYUzzHPUFH7FnnuxB4jCS9JE7dNJXaipoUjAWPGHm",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "EFVYYfVGhj8mzQio7Fr7DbWqZTzK3KFC99rreeYzRZN",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/YHey5YM4yr5BhpEDX-fq5fyPTkGbE679J0HEHM7DY-Y?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Black Hole"
        },
        {
          "trait_type": "Background",
          "value": "Trader Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Jimmy Neutron"
        },
        {
          "trait_type": "Desk",
          "value": "Weathered"
        },
        {
          "trait_type": "Shelf",
          "value": "Scorched"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Record Player"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Smartwatch"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Ledger"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Angry"
        },
        {
          "trait_type": "Hair",
          "value": "Nerd Side Part"
        },
        {
          "trait_type": "Glasses",
          "value": "Classic Shades"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Turquoise Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Business Developer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/YHey5YM4yr5BhpEDX-fq5fyPTkGbE679J0HEHM7DY-Y?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T20:13:18.748Z",
      "updatedAt": "2023-03-05T20:13:18.748Z"
    },
    {
      "mintAddress": "AjpnLAusLRMDz9EXAiWL2qxecK7BUGRZ1rQ1q4HGq1B6",
      "supply": 1,
      "title": "Entreprenerdz #1615",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.25,
      "escrowPubkey": "7eWjE5reKgU5Kb76ZAhB2vuVRix3Vz8GQqNk1Erxrimh",
      "owner": "5v7kVsf1MLfwouoKoJ7uSswN75hnUFBn1LpLB4Eqnqu2",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "5GMFvYkdQKWoKBjyXbpMoUw1wR2y55udp8iosi89tyVd",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/_Q_RsS7wa7LYECD-rKrdigjxk9bijs-9jGdO5mCQ-uY?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Crystals"
        },
        {
          "trait_type": "Background",
          "value": "Normie"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "Kimono"
        },
        {
          "trait_type": "Desk",
          "value": "Gum"
        },
        {
          "trait_type": "Shelf",
          "value": "Mosaic"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Open Neon"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Medicine Bottle"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Rubiks Cube"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Smoking Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Newsboy Cap"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Compact Black"
        },
        {
          "trait_type": "Profession",
          "value": "Artist"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/_Q_RsS7wa7LYECD-rKrdigjxk9bijs-9jGdO5mCQ-uY?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T20:54:36.424Z",
      "updatedAt": "2023-03-05T20:54:36.424Z"
    },
    {
      "mintAddress": "ythEWHQNs6oobK9oWpwUKo6vbgiL1S7LtPsSfNZPwh6",
      "supply": 1,
      "title": "Entreprenerdz #6046",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.25,
      "escrowPubkey": "GRMCSRwb2KwYi4ky1EmVHbLRh7Lnfip8Y8APyRWtkkfY",
      "owner": "7q6vYUzzHPUFH7FnnuxB4jCS9JE7dNJXaipoUjAWPGHm",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "BLNaQicJJ5Gv9LvhcJyTV8cPfDPsKJU61WzqoA3Gi3yj",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/n8Vvxd2RBxHClMkcc6BoMr9M5L3GJXy4RVQFBCXr2Ac?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Tropical"
        },
        {
          "trait_type": "Background",
          "value": "Dungeon"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Medium"
        },
        {
          "trait_type": "Clothes",
          "value": "White Robe"
        },
        {
          "trait_type": "Desk",
          "value": "Cherry Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Metal"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Katana"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Film Camera"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Blowtorch"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Suggestive Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Rock N' Roll Golden"
        },
        {
          "trait_type": "Glasses",
          "value": "Dwight"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Turquoise Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Artist"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/n8Vvxd2RBxHClMkcc6BoMr9M5L3GJXy4RVQFBCXr2Ac?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T21:18:35.751Z",
      "updatedAt": "2023-03-05T21:18:35.751Z"
    },
    {
      "mintAddress": "Bo8QVjw7hV9NAQK4DVkS9DVmoZ1767CeQfUtwhC51V43",
      "supply": 1,
      "title": "Entreprenerdz #1485",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.25,
      "escrowPubkey": "Br8akMnD8G9gy86CXUd7VYMrFxvjmyTam4HYFLuiqB9i",
      "owner": "8FFdNmtjqYRZmuW2TBFM5gq72N3eHPStJ2U8syHsuUP9",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "73qeDwSUpdrdrSX2SneQoemWFKFZ4XC7ytP5mZRM1HuS",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/t7s245qlcsiNhLwWmlMBDutPn12qbt8l4yHzfg4oyiA?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Game Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "Leather Jacket"
        },
        {
          "trait_type": "Desk",
          "value": "Weathered"
        },
        {
          "trait_type": "Shelf",
          "value": "Cut Stone"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Hookah"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Smartwatch"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Test Tube"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Wicked"
        },
        {
          "trait_type": "Hair",
          "value": "Nerd Side Part"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Compact Black"
        },
        {
          "trait_type": "Profession",
          "value": "Accountant"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/t7s245qlcsiNhLwWmlMBDutPn12qbt8l4yHzfg4oyiA?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T22:33:18.742Z",
      "updatedAt": "2023-03-05T22:33:18.742Z"
    },
    {
      "mintAddress": "41DVeFJRWVyK9ayGZtTCk74zv87P4Z5bJJA3Wjq5kGTc",
      "supply": 1,
      "title": "Entreprenerdz #6103",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.260686453,
      "escrowPubkey": "5ToHR9yfNJHowET3zPyJzYDMEZmunje1mefHZCx6gV5N",
      "owner": "DKVJeggxTCcuZCGsRF4aWR28awzXkDwDq17wtTemAdAb",
      "id": "BoY1iCyAEa7M4mGN4G4c566zfNH3JTnKCPT2rsEMfYHM",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/8CHZGRV7wPzrdW20op3j4ErvuG__JX0H_DALLcSUQm0?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Tropical"
        },
        {
          "trait_type": "Background",
          "value": "D&D"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "Stay Focused"
        },
        {
          "trait_type": "Desk",
          "value": "Weathered"
        },
        {
          "trait_type": "Shelf",
          "value": "Mosaic"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Saber Blue"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Ramen"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Light Therapy Lamp"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "WTF"
        },
        {
          "trait_type": "Hair",
          "value": "Boyish Black"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Classic White"
        },
        {
          "trait_type": "Profession",
          "value": "Entrepreneur"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/8CHZGRV7wPzrdW20op3j4ErvuG__JX0H_DALLcSUQm0?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "amm": {
        "poolKey": "EGfQVMKJH9rjKbKa4AWfsn4sGvToJm1xqndZk27nrKA",
        "source": "coral_cube_v2",
        "spotPrice": 2069999999,
        "curveType": "exp",
        "curveDelta": 100,
        "lpFeeBp": 600,
        "poolType": "two_sided",
        "nextSpotPrice": 2132723068.969699,
        "mmmPoolRank": 2
      },
      "createdAt": "2023-03-05T19:35:21.813Z",
      "updatedAt": "2023-03-05T19:35:21.813Z"
    },
    {
      "mintAddress": "5LMee7K2PmiesfQTeTNtLwUuqWzSHrFy37r8kk7SVda5",
      "supply": 1,
      "title": "Entreprenerdz #8708",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.268071998,
      "escrowPubkey": "AGk9iPwBLcBmD4RU9h4Mu3aurnAAeJBfEKBzSDxvYSYb",
      "owner": "HiH4fkQSXfrtU9tVv7boG2QDMxVw5yi9M56L7VqL8vBD",
      "id": "ALaWCAQA2hYYHe4gWAjiyEBbTDBBgNH3eSHYAg4cdob4",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/qOHIKeh9smLgVH9YCQ_ZNg1sb8aGHzJl-IkQwasDwwk?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Castle"
        },
        {
          "trait_type": "Background",
          "value": "Anime Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Jersey"
        },
        {
          "trait_type": "Desk",
          "value": "Weathered"
        },
        {
          "trait_type": "Shelf",
          "value": "Galaxy"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Saber Blue"
        },
        {
          "trait_type": "Desk Prop",
          "value": "VR Controllers"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Bong"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Suggestive Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Bowl Golden"
        },
        {
          "trait_type": "Glasses",
          "value": "Classic Shades"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Compact White"
        },
        {
          "trait_type": "Profession",
          "value": "Artist"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/qOHIKeh9smLgVH9YCQ_ZNg1sb8aGHzJl-IkQwasDwwk?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "amm": {
        "poolKey": "36WHyK24d2WwLBTiXX4KPL4ueXkNjHgmfpDEpBn8Pdig",
        "source": "coral_cube_v2",
        "spotPrice": 2137254901,
        "curveType": "exp",
        "curveDelta": 200,
        "lpFeeBp": 400,
        "poolType": "sell_sided",
        "nextSpotPrice": 2268071998.980408,
        "mmmPoolRank": 2
      },
      "createdAt": "2023-03-05T17:44:39.747Z",
      "updatedAt": "2023-03-05T17:44:39.747Z"
    },
    {
      "mintAddress": "9yvr1dPVtsCkd9syqFyHuudzstVYfcro3AoLS6NEqKjn",
      "supply": 1,
      "title": "Entreprenerdz #4825",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.283293317,
      "escrowPubkey": "g5XBMzqBh3p23uzgK4msVvKkqvm2zPSKjASsS9DubpH",
      "owner": "DKVJeggxTCcuZCGsRF4aWR28awzXkDwDq17wtTemAdAb",
      "id": "74b9hKvCtYAce2dkTPDd1yKPvUvb2e3BZizpfNSfoXDu",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/cSB2oDl1-vB5256YtvTY0eOreU8VLHD5SBrbdns5fBs?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Music Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Fair"
        },
        {
          "trait_type": "Clothes",
          "value": "Denim Jacket"
        },
        {
          "trait_type": "Desk",
          "value": "Cardboard"
        },
        {
          "trait_type": "Shelf",
          "value": "Galaxy"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Helmet"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Water Bottle"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Wallet & Keys"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Suggestive"
        },
        {
          "trait_type": "Hair",
          "value": "Torn Hat"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Switch"
        },
        {
          "trait_type": "Profession",
          "value": "Artist"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/cSB2oDl1-vB5256YtvTY0eOreU8VLHD5SBrbdns5fBs?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "amm": {
        "poolKey": "EGfQVMKJH9rjKbKa4AWfsn4sGvToJm1xqndZk27nrKA",
        "source": "coral_cube_v2",
        "spotPrice": 2069999999,
        "curveType": "exp",
        "curveDelta": 100,
        "lpFeeBp": 600,
        "poolType": "two_sided",
        "nextSpotPrice": 2154050299.659396,
        "mmmPoolRank": 3
      },
      "createdAt": "2023-03-05T18:11:18.183Z",
      "updatedAt": "2023-03-05T18:11:18.183Z"
    },
    {
      "mintAddress": "3JYSm5FHtZ9RLAwxzeEuFmFVPDnMtncjsMwtVy4GscoP",
      "supply": 1,
      "title": "Entreprenerdz #9015",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.29,
      "escrowPubkey": "ANLruhzWDYrUTGRJiHFp41rHwyCjEgf4J2xm7xm9jRuY",
      "owner": "HoFQFQSBmVr9aGS1VUkv12SKLwctFLusTFfQkuboYU7U",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "AuXiHJyQZ4GnNS7iwPvRsipS6NwASQN6Hb1sVR4cuoum",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/1FuRwHN-GbJpvZgfT_7G69Wm3dwj8mfci0gB4y3wrm0?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Castle"
        },
        {
          "trait_type": "Background",
          "value": "Degenformers"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Lab Coat"
        },
        {
          "trait_type": "Desk",
          "value": "Weathered"
        },
        {
          "trait_type": "Shelf",
          "value": "Metal"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Chance"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Beer Bottle"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Blowtorch"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Smoking Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Mullet Golden"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Turquoise Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Artist"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/1FuRwHN-GbJpvZgfT_7G69Wm3dwj8mfci0gB4y3wrm0?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T21:03:07.071Z",
      "updatedAt": "2023-03-05T21:03:07.071Z"
    },
    {
      "mintAddress": "DjiRBTXz332nXXx6mPCqZwgcd3gBRZao6hBmrvHJd5zn",
      "supply": 1,
      "title": "Entreprenerdz #4387",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.2984,
      "escrowPubkey": "ozi5GNoEUeP6GNMkLtr9T1U2U8g2eSErVfe21WAzG7Z",
      "owner": "perce3N2p5LSHcKS8AUpzqgogvNaiQc1zMapfuKRdBx",
      "id": "AtygopicwB2uDBdeGu9TgsuuXXHcXjLTEutfhx1MnQeZ",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/klcMy1pjbaBKRs3fzvMLTm0gaiO1IHplLonY04Rw14E?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Music Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Medium"
        },
        {
          "trait_type": "Clothes",
          "value": "Overalls"
        },
        {
          "trait_type": "Desk",
          "value": "Plum Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Colorful Marble"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Medication"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Smartwatch"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Wallet & Keys"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Meh Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Mullet Golden"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Snow Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Degen"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/klcMy1pjbaBKRs3fzvMLTm0gaiO1IHplLonY04Rw14E?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "amm": {
        "poolKey": "2iEvHywd5pvtcnDmHrZh6wQELhbBZHrGZ6456aWempPU",
        "source": "coral_cube_v2",
        "spotPrice": 2000000000,
        "curveType": "linear",
        "curveDelta": 70000000,
        "lpFeeBp": 400,
        "poolType": "two_sided",
        "nextSpotPrice": 2210000000,
        "mmmPoolRank": 2
      },
      "createdAt": "2023-03-05T17:32:36.133Z",
      "updatedAt": "2023-03-05T17:32:36.133Z"
    },
    {
      "mintAddress": "7g639JED4jfMFQ2S3yCPsHdRziVBPFJUt6eNcxFjDGkW",
      "supply": 1,
      "title": "Entreprenerdz #2266",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.3,
      "escrowPubkey": "E7KvhFmtusPCg6Km2QxXa5t3aGTeAFLYDEMBL19qc3EP",
      "owner": "GMnqRGT2vhqZ4e27mvJVW8NidvQfaxk2zHxpJtTvkuJH",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "3Ad2DrHch5GkSD7HXGKDq682aR5ZtsHdaVDfTxKxUTdc",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/Tz1F030-h05oKk_2vHX88LhlpCSjVhLF9FCjSbqkiYM?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Black Hole"
        },
        {
          "trait_type": "Background",
          "value": "Cozy Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "Boobs"
        },
        {
          "trait_type": "Desk",
          "value": "Oak"
        },
        {
          "trait_type": "Shelf",
          "value": "Iron Vein"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Sparky"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Ashtray"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Ledger"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "WTF"
        },
        {
          "trait_type": "Hair",
          "value": "Rock N' Roll Golden"
        },
        {
          "trait_type": "Glasses",
          "value": "Classic Shades"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Rose Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Business Developer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/Tz1F030-h05oKk_2vHX88LhlpCSjVhLF9FCjSbqkiYM?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T18:18:49.373Z",
      "updatedAt": "2023-03-05T18:18:49.373Z"
    },
    {
      "mintAddress": "GTqyyTaZVEeUnkoYF35c8UyvN4NipYBCnYrQMh3qWKyF",
      "supply": 1,
      "title": "Entreprenerdz #2085",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.3,
      "escrowPubkey": "3GmSixP1bSYWucmz272Beh6tTFwiVo1SzfyLWzSmKskW",
      "owner": "HN3n44GjhZV6RM9p6x52a3MtFzKDFGLCAQa1WqyniRte",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "CFNNTBmoe45DGTog7ibnWAnGDCvGf4jbbKs8HNeXNuo6",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/w15a_hBEVdjjS431k6rfcikZM-s8OMT9A7Nyh13yD-0?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Trash Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "Giga Polo"
        },
        {
          "trait_type": "Desk",
          "value": "Gum"
        },
        {
          "trait_type": "Shelf",
          "value": "Metal"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Hookah"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Toilet Paper"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Bong"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Sheepish"
        },
        {
          "trait_type": "Hair",
          "value": "Bowl Auburn"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "RGB"
        },
        {
          "trait_type": "Profession",
          "value": "Accountant"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/w15a_hBEVdjjS431k6rfcikZM-s8OMT9A7Nyh13yD-0?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T22:13:00.359Z",
      "updatedAt": "2023-03-05T22:13:00.359Z"
    },
    {
      "mintAddress": "9zeZ5DMbCTrdLnXKwHgtMARimqN5RCJ42myrZpoz87Ka",
      "supply": 1,
      "title": "Entreprenerdz #2223",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.3,
      "escrowPubkey": "5PhV1zvhd3EgYR7w6eazT61ywqamtXFHSoCvVU5AWBv7",
      "owner": "BwMWSZk9fBm6Vr8NNVTYc44w6KGQpjisdAXXyiJTwMw2",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "64WZjhCMSDQLZBBCexUwYX2i6Wqb6Et1h2nmNDNVdMJM",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/9JzDjKYG2n-7Sex4Ehd6CeeBfvxHqEXMs1mWkeKe5V8?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Music Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Beatz by Nerdz"
        },
        {
          "trait_type": "Desk",
          "value": "Weathered"
        },
        {
          "trait_type": "Shelf",
          "value": "Ocean Sound"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Pyramid"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Quill & Ink"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Light Therapy Lamp"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Shook"
        },
        {
          "trait_type": "Hair",
          "value": "Cropped Afro"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Wired Black"
        },
        {
          "trait_type": "Profession",
          "value": "Accountant"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/9JzDjKYG2n-7Sex4Ehd6CeeBfvxHqEXMs1mWkeKe5V8?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T20:51:30.442Z",
      "updatedAt": "2023-03-05T20:51:30.442Z"
    },
    {
      "mintAddress": "5yqetmDLaHPmiaAoPn9c4uvFwMKrcf7tL5HSSDUt4qrb",
      "supply": 1,
      "title": "Entreprenerdz #6392",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.3,
      "escrowPubkey": "DHrFomfA2bcfEgbUTHnbBkXQkgPtv63wQk7Xnvcc8HNY",
      "owner": "5v7kVsf1MLfwouoKoJ7uSswN75hnUFBn1LpLB4Eqnqu2",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "4rRoAPgoRuY4PvpmSvcJ5vctpfnKh6gc7cwnZWz8wTyv",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/jBno5dM-0pbGMq-JUVjRhUHpjYFGakMONikHKRHD3AU?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Castle"
        },
        {
          "trait_type": "Background",
          "value": "Normie"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Fair"
        },
        {
          "trait_type": "Clothes",
          "value": "Linked"
        },
        {
          "trait_type": "Desk",
          "value": "Gum"
        },
        {
          "trait_type": "Shelf",
          "value": "Geode"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Stop Sign"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Smartwatch"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "TV Remote"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Meh Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Nerd Side Part"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Rose Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Accountant"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/jBno5dM-0pbGMq-JUVjRhUHpjYFGakMONikHKRHD3AU?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T20:52:59.561Z",
      "updatedAt": "2023-03-05T20:52:59.561Z"
    },
    {
      "mintAddress": "BLAhPqjiBh9YMMpsELSQvsqm98BP5Zy4UhDnpfJsLckc",
      "supply": 1,
      "title": "Entreprenerdz #4234",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.3,
      "escrowPubkey": "3DzUPQJXPsECZ5jERbmLTC9FgEiYnjXP55gA8aoZWuTd",
      "owner": "9NxQEFLFZyrNRsHncwSTLuSA8ryih1wxBkU6gkG5ScCi",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "DaEU7P3GLqjeYCXTTfsif6SjAgjahYFSjnSmN3w6X3qF",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/nCuC7mkbT0yLXzB5SHIyLKLgNQjNg5mCf-jfYHxbAMc?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Space"
        },
        {
          "trait_type": "Background",
          "value": "Trader Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "Agent S"
        },
        {
          "trait_type": "Desk",
          "value": "Cherry Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Wood"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Plant Paradise"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Smartwatch"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Iphone & Airpods"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Suggestive Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Undercut"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Classic White"
        },
        {
          "trait_type": "Profession",
          "value": "Business Developer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/nCuC7mkbT0yLXzB5SHIyLKLgNQjNg5mCf-jfYHxbAMc?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T22:22:23.722Z",
      "updatedAt": "2023-03-05T22:22:23.722Z"
    },
    {
      "mintAddress": "Ce4oWRf6jwuWhYdiUMjw7sNh5uMEQzgPUsF9ujTuXsYa",
      "supply": 1,
      "title": "Entreprenerdz #4915",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.3,
      "escrowPubkey": "BaYRCGpLK3sVuXRBNDRWgGZk5HKp8zAyg3aBv8ek8Gr2",
      "owner": "HvQY32oab4nwtDwabkKtMs2PJpmdNifBUA5CThR85mK",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "5MbThe2ikszWjsrsYu1Pdh1vz9fS5AsGGEYwLyw1Vi4n",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/AQYjo--VRyoKTrPwy-LzH-kFUO7TIOeeQBEPE7UZBxA?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Mom's Basement"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Dark Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Jock"
        },
        {
          "trait_type": "Desk",
          "value": "Weathered"
        },
        {
          "trait_type": "Shelf",
          "value": "Metal"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Books"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Film Camera"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Ledger"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Happy Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Mullet Golden"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Rose Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Marketer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/AQYjo--VRyoKTrPwy-LzH-kFUO7TIOeeQBEPE7UZBxA?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T22:56:15.653Z",
      "updatedAt": "2023-03-05T22:56:15.653Z"
    },
    {
      "mintAddress": "FcCv9fWiYeYkMHkDHcaMc48HPibQ5f9ZdUpefscrWFMo",
      "supply": 1,
      "title": "Entreprenerdz #1253",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.3052,
      "escrowPubkey": "AgR2SZvywdzd7jgQAyUZazLCStLq8SnLWbkdd7w3jrjW",
      "owner": "6p9MtdE6Fau4Q2LrP97WWxrMXMVK9QvsmrVfcMCxuj5D",
      "id": "C1ckwTXwhwmU5meLzhwCirqxzvsEzaDf5aVNpYgc1Vu5",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/Q3q71UBEfSZjsgzo0cQzjlJW9KBS556qfBf9pl5gH7A?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Crystals"
        },
        {
          "trait_type": "Background",
          "value": "Normie"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Medium"
        },
        {
          "trait_type": "Clothes",
          "value": "Black Jacket"
        },
        {
          "trait_type": "Desk",
          "value": "Plum Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Malachite"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Record Player"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Giga Mecha"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Speaker"
        },
        {
          "trait_type": "Blemish",
          "value": "Freckles 1"
        },
        {
          "trait_type": "Expression",
          "value": "Suggestive"
        },
        {
          "trait_type": "Hair",
          "value": "Bowl Auburn"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Wired Black"
        },
        {
          "trait_type": "Profession",
          "value": "Entrepreneur"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/Q3q71UBEfSZjsgzo0cQzjlJW9KBS556qfBf9pl5gH7A?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "amm": {
        "poolKey": "AVVymU7mCxW6gb3p9VHB8MVbinLChxVxrheDxuCxeTBz",
        "source": "coral_cube_v2",
        "spotPrice": 1980000000,
        "curveType": "linear",
        "curveDelta": 70000000,
        "lpFeeBp": 200,
        "poolType": "two_sided",
        "nextSpotPrice": 2260000000,
        "mmmPoolRank": 3
      },
      "createdAt": "2023-03-05T18:13:37.065Z",
      "updatedAt": "2023-03-05T18:13:37.065Z"
    },
    {
      "mintAddress": "ASj5zrX3EQKdtxFenKBQb5wXDG3fPudJqsqdarPjgVsT",
      "supply": 1,
      "title": "Entreprenerdz #7435",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.30612625,
      "escrowPubkey": "EsYgeo1ExjyHXR5V5rhG7DzJtGxn4u1Lm3NNjxoKwmLm",
      "owner": "DKVJeggxTCcuZCGsRF4aWR28awzXkDwDq17wtTemAdAb",
      "id": "43rwdNgT6GYbY2pH9BWEuazSH7murWef8zEhRvwpeSTa",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/n9_NDkn9isnROL8m43BkvCTZ0jUyl2pOx71pv2L6ZM4?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Trash Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Medium"
        },
        {
          "trait_type": "Clothes",
          "value": "Agent S"
        },
        {
          "trait_type": "Desk",
          "value": "Weathered"
        },
        {
          "trait_type": "Shelf",
          "value": "Metal"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Sparky"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Smartwatch"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Frog Incense"
        },
        {
          "trait_type": "Blemish",
          "value": "Freckles 2"
        },
        {
          "trait_type": "Expression",
          "value": "Scared"
        },
        {
          "trait_type": "Hair",
          "value": "Red Fox"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Rose Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Artist"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/n9_NDkn9isnROL8m43BkvCTZ0jUyl2pOx71pv2L6ZM4?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "amm": {
        "poolKey": "EGfQVMKJH9rjKbKa4AWfsn4sGvToJm1xqndZk27nrKA",
        "source": "coral_cube_v2",
        "spotPrice": 2069999999,
        "curveType": "exp",
        "curveDelta": 100,
        "lpFeeBp": 600,
        "poolType": "two_sided",
        "nextSpotPrice": 2175590802.65599,
        "mmmPoolRank": 4
      },
      "createdAt": "2023-03-05T18:12:46.293Z",
      "updatedAt": "2023-03-05T18:12:46.293Z"
    },
    {
      "mintAddress": "GKAknp3XLHLTWQx6zJVARz5ZLFEThMkye8LHZhfsaP2p",
      "supply": 1,
      "title": "Entreprenerdz #5850",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.313131313,
      "escrowPubkey": "Ch4QasNyXqxS4iSxKJtaQypdrP81akAGvEwDCTvs9ArE",
      "owner": "hadeaC5JQvAJugvsa97BPPSdeGQzhWxqK6DAqq5TsW8",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "CX3t2Gx1wo9Ae28TibiYfnA7uBYsAMwhP2UC42aKqxFn",
        "expiry": -1
      },
      "id": "3CWSZ59pFri4L8Y1BTksWL8tifgWF2HgMrubZsEcyG57",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/lR9RniyKF3Z1RoZDn8Nwssn8MxQJKdNdS7OAdpe1_PU?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Tropical"
        },
        {
          "trait_type": "Background",
          "value": "Trader Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Dark Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Flannel"
        },
        {
          "trait_type": "Desk",
          "value": "Oak"
        },
        {
          "trait_type": "Shelf",
          "value": "Geode"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Scythe"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Medicine Bottle"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Desk Mic"
        },
        {
          "trait_type": "Blemish",
          "value": "Freckles 2"
        },
        {
          "trait_type": "Expression",
          "value": "Strained"
        },
        {
          "trait_type": "Hair",
          "value": "Mullet Brown"
        },
        {
          "trait_type": "Glasses",
          "value": "Broken Nerd"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Rose Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Degen"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/lR9RniyKF3Z1RoZDn8Nwssn8MxQJKdNdS7OAdpe1_PU?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T19:17:06.043Z",
      "updatedAt": "2023-03-05T19:17:06.043Z"
    },
    {
      "mintAddress": "64n8rVg6nmHJu4FR6o6h3hEqfRKuvLK2gi7jrtMwRp1o",
      "supply": 1,
      "title": "Entreprenerdz #2981",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.329187513,
      "escrowPubkey": "J4HK1UawHD6uQH8AfXevXvKfdqFbRxMr3Z8XqmABUREH",
      "owner": "DKVJeggxTCcuZCGsRF4aWR28awzXkDwDq17wtTemAdAb",
      "id": "2MSwcnChXW1rWsgn7jAEgEGJmwNcqdMrRov5sveGU9YL",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/GkII6OCiqrTXNh9pJXn7WPdfLr8rzdf-Q0lndJ-e6Ak?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Suburbs"
        },
        {
          "trait_type": "Background",
          "value": "Degenformers"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Boobs"
        },
        {
          "trait_type": "Desk",
          "value": "Cherry Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Mosaic"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Record Player"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Beer Bottle"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Frog Incense"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Smoking"
        },
        {
          "trait_type": "Hair",
          "value": "Torn Hat"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "RGB"
        },
        {
          "trait_type": "Profession",
          "value": "Marketer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/GkII6OCiqrTXNh9pJXn7WPdfLr8rzdf-Q0lndJ-e6Ak?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "amm": {
        "poolKey": "EGfQVMKJH9rjKbKa4AWfsn4sGvToJm1xqndZk27nrKA",
        "source": "coral_cube_v2",
        "spotPrice": 2069999999,
        "curveType": "exp",
        "curveDelta": 100,
        "lpFeeBp": 600,
        "poolType": "two_sided",
        "nextSpotPrice": 2197346710.68255,
        "mmmPoolRank": 5
      },
      "createdAt": "2023-03-05T18:10:24.069Z",
      "updatedAt": "2023-03-05T18:10:24.069Z"
    },
    {
      "mintAddress": "71Dcx3tYPbYihAojgs3PkqoyCQVCQM7KsDmGMUBisa3V",
      "supply": 1,
      "title": "Entreprenerdz #2763",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.33,
      "escrowPubkey": "7F1XVSYDEXzjFBxwwDiU3tNMxM5fJh9oBKZ9chAjhcLQ",
      "owner": "BtbxfyPx5v82dcKYZTU73Nww9esX1T31t9TPjSw4LuXp",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "67ZBnDFDG5Ux1o4FTuKF1FXTxbVEHz6LmCnWKU5LY6NN",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/iCcDEAQoohL9zpjfEMI6ll6julc3VcZj-eJZsFaJAcE?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Music Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Dark Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Black Jacket"
        },
        {
          "trait_type": "Desk",
          "value": "Gum"
        },
        {
          "trait_type": "Shelf",
          "value": "Galaxy"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Father of Dragons"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Game Controller"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Frog Incense"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Suggestive"
        },
        {
          "trait_type": "Hair",
          "value": "Nerd Side Part"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "Black"
        },
        {
          "trait_type": "Keyboard",
          "value": "Rose Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Entrepreneur"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/iCcDEAQoohL9zpjfEMI6ll6julc3VcZj-eJZsFaJAcE?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T20:52:58.468Z",
      "updatedAt": "2023-03-05T20:52:58.468Z"
    },
    {
      "mintAddress": "458mGf9f1xQvoqumrR1V8NJHEWwof9jfoFgCi61uj5hn",
      "supply": 1,
      "title": "Entreprenerdz #1617",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.33,
      "escrowPubkey": "4c3QzVtJC5oBgBATA8WSVBYfEttsnmCbKmTGqnyRsefF",
      "owner": "BtbxfyPx5v82dcKYZTU73Nww9esX1T31t9TPjSw4LuXp",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "4HsMY3QmUwipo1z2DQjCUueAzmyHNezupTuyQZyoLe4K",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/OFV_MQOPCmqPUq_jEFdlouvxxtSALiXlQFE69KjstWo?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Black Hole"
        },
        {
          "trait_type": "Background",
          "value": "Normie"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "Fallout"
        },
        {
          "trait_type": "Desk",
          "value": "Weathered"
        },
        {
          "trait_type": "Shelf",
          "value": "Ocean Sound"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Troop"
        },
        {
          "trait_type": "Desk Prop",
          "value": "GigaPower"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "TV Remote"
        },
        {
          "trait_type": "Blemish",
          "value": "Blush"
        },
        {
          "trait_type": "Expression",
          "value": "Satisfied"
        },
        {
          "trait_type": "Hair",
          "value": "Dreads"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Classic White"
        },
        {
          "trait_type": "Profession",
          "value": "Artist"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/OFV_MQOPCmqPUq_jEFdlouvxxtSALiXlQFE69KjstWo?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T20:52:57.673Z",
      "updatedAt": "2023-03-05T20:52:57.673Z"
    },
    {
      "mintAddress": "E4tkvswqNH6SLaxrqrsBg66cLHTtGrwFjy6rubN2uqPo",
      "supply": 1,
      "title": "Entreprenerdz #7424",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.33,
      "escrowPubkey": "3no3EEFGiUkuZJ8PZuBSxrZYGe9KyEzqdMdgGnxaAVcB",
      "owner": "Enochf5h8U4GGrCyepYoJ5nwcy8kwNmNuzBdX1yb9Kwa",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "3CduqT8yMK2C26MeCMNnChSAsTZKth7N5F49417QkmTL",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/Oke5GJuHGJqMp6NuZjRYnAhMh1n9qyUALDwIynftu2g?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Music Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Fair"
        },
        {
          "trait_type": "Clothes",
          "value": "Health"
        },
        {
          "trait_type": "Desk",
          "value": "Oak"
        },
        {
          "trait_type": "Shelf",
          "value": "Iron Vein"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Scythe"
        },
        {
          "trait_type": "Desk Prop",
          "value": "VR Controllers"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Ledger"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Smoking"
        },
        {
          "trait_type": "Hair",
          "value": "GigaDAO Hat"
        },
        {
          "trait_type": "Glasses",
          "value": "Classic Shades"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Snow Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Business Developer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/Oke5GJuHGJqMp6NuZjRYnAhMh1n9qyUALDwIynftu2g?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T21:37:03.069Z",
      "updatedAt": "2023-03-05T21:37:03.069Z"
    },
    {
      "mintAddress": "FMLZSwj3crpde1nDT2H3GV5TRyFcXKaqidyEyRyB86ER",
      "supply": 1,
      "title": "Entreprenerdz #1477",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.34,
      "escrowPubkey": "9B1vxsizPdSRtecoteGPoH2tw94qrQ9soA2wYG1hyefe",
      "owner": "7LyfwfUPLdYVMGMhnEBZf23taEfnfgsjXTAhM2vp7aTz",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "6YK77jX5a3btGQQ9Zi4HGy9eLwEUemRztivm4QGfCsV5",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/FQWLthgw1X4DXPIMs7_5EJDmFtd09fHgHw0UyOn689k?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Trash Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "Kimono"
        },
        {
          "trait_type": "Desk",
          "value": "Oak"
        },
        {
          "trait_type": "Shelf",
          "value": "Ocean Sound"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Record Player"
        },
        {
          "trait_type": "Desk Prop",
          "value": "GigaPower"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Speaker"
        },
        {
          "trait_type": "Blemish",
          "value": "Freckles 1"
        },
        {
          "trait_type": "Expression",
          "value": "Smoking Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Messy"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Compact White"
        },
        {
          "trait_type": "Profession",
          "value": "Artist"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/FQWLthgw1X4DXPIMs7_5EJDmFtd09fHgHw0UyOn689k?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T17:53:42.619Z",
      "updatedAt": "2023-03-05T17:53:42.619Z"
    },
    {
      "mintAddress": "7rfXqYLc1noMTWAaT5RFdGBc2RBesnCEwbwP8gHd7dBx",
      "supply": 1,
      "title": "Entreprenerdz #7721",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.34,
      "escrowPubkey": "BYLd2xHGuUKNNpsWcP52FWxcD9PSeUeA75GaSc3TRdnE",
      "owner": "HH5oT2AvhS2iyd4J1jGoaWiCbC5zzbpmehCsKSXdcjnB",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "Dvj22zLg52H816dF7jeoxX2ZqMhsfPHWL4XxGFNitFB5",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/DkPISDC4juSaR7ppdEBN7W_Rff951q38Lu8plwjn6go?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Castle"
        },
        {
          "trait_type": "Background",
          "value": "Penthouse"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Fair"
        },
        {
          "trait_type": "Clothes",
          "value": "Jersey"
        },
        {
          "trait_type": "Desk",
          "value": "Oak"
        },
        {
          "trait_type": "Shelf",
          "value": "Ocean Sound"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Record Player"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Calculator"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Blowtorch"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Scared Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Mullet Golden"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Snow Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Marketer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/DkPISDC4juSaR7ppdEBN7W_Rff951q38Lu8plwjn6go?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T17:54:59.560Z",
      "updatedAt": "2023-03-05T17:54:59.560Z"
    },
    {
      "mintAddress": "HmzKVo5nJXxhuBWALqQ8NKGRs25fFwXhFj898PFEBXZt",
      "supply": 1,
      "title": "Entreprenerdz #8632",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.35,
      "escrowPubkey": "6cwHCfBnn7hotZ36XhHXdp2hcLaYJyPNddj5XqnXPTeC",
      "owner": "9ZuQFTrSapQA7vFcokwcUAeTUPhZyHZLp7QqyQLtwvDp",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "BkSVkE5QRGC37JYW1pLRyLuNrP4d6sGuNTYusbyeLeWj",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/wdax70h-GEZvWnTRolgFOV3RTx-qba5kz-Z44iSoJKw?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Castle"
        },
        {
          "trait_type": "Background",
          "value": "Cozy Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Fair"
        },
        {
          "trait_type": "Clothes",
          "value": "Giga Polo"
        },
        {
          "trait_type": "Desk",
          "value": "Oak"
        },
        {
          "trait_type": "Shelf",
          "value": "Iron Vein"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Harley Davidson"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Glasses & Case"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Playman"
        },
        {
          "trait_type": "Blemish",
          "value": "Acne"
        },
        {
          "trait_type": "Expression",
          "value": "Suggestive Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Newsboy Cap"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Tablet"
        },
        {
          "trait_type": "Profession",
          "value": "Marketer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/wdax70h-GEZvWnTRolgFOV3RTx-qba5kz-Z44iSoJKw?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T17:57:44.041Z",
      "updatedAt": "2023-03-05T17:57:44.041Z"
    },
    {
      "mintAddress": "HoqsBDiGYkNhGEKdz4637atsnstQhpJBNgbJ24c5odZ4",
      "supply": 1,
      "title": "Entreprenerdz #2933",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.35,
      "escrowPubkey": "5pXg825tSLrcZVbEfHiYMvpdYSfncZ7eEfKiwf2qHysJ",
      "owner": "9ZuQFTrSapQA7vFcokwcUAeTUPhZyHZLp7QqyQLtwvDp",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "D5N3S1zk5KH9w4jcLaPvAsstM4P2MP2LqmLSg2qGBKUo",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/-pFREED-m8djc1MLDfiuvV-Qjmj1HTwvDOY2buLnqc4?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Suburbs"
        },
        {
          "trait_type": "Background",
          "value": "Trader Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Medium"
        },
        {
          "trait_type": "Clothes",
          "value": "Stay Focused"
        },
        {
          "trait_type": "Desk",
          "value": "Cherry Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Metal"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Open Neon"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Ramen"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Tesseract"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Satisfied"
        },
        {
          "trait_type": "Hair",
          "value": "Greasy Long"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Classic White"
        },
        {
          "trait_type": "Profession",
          "value": "Business Developer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/-pFREED-m8djc1MLDfiuvV-Qjmj1HTwvDOY2buLnqc4?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T17:56:41.665Z",
      "updatedAt": "2023-03-05T17:56:41.665Z"
    },
    {
      "mintAddress": "4zmhgsTuKr8g9NgPAwCAg6fjFUd35XBmnjSrS2NnDz9V",
      "supply": 1,
      "title": "Entreprenerdz #6374",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.35,
      "escrowPubkey": "EqvQZyoeszWD5DkEWa9YoNnTDd5vjBUcDPXNvifvz9o9",
      "owner": "FQXc2ZhRzMxU6UTa8zuRabEQpdfYhNjPzDoZq53xx5Bx",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "EfoLeGmwdQLTDGnQaABVyBs6yvjShiGShJPwMz7yBd4a",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/sKrPWfPKzx_SiCVd86cIqs0q8gIqnpOdxa5-e52GkRE?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Space"
        },
        {
          "trait_type": "Background",
          "value": "Normie"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Fair"
        },
        {
          "trait_type": "Clothes",
          "value": "Flannel"
        },
        {
          "trait_type": "Desk",
          "value": "Gum"
        },
        {
          "trait_type": "Shelf",
          "value": "Lava Core"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Open Neon"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Microscope"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Space Shuttle"
        },
        {
          "trait_type": "Blemish",
          "value": "Freckles 2"
        },
        {
          "trait_type": "Expression",
          "value": "Wicked"
        },
        {
          "trait_type": "Hair",
          "value": "Nerd Side Part"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Switch"
        },
        {
          "trait_type": "Profession",
          "value": "Entrepreneur"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/sKrPWfPKzx_SiCVd86cIqs0q8gIqnpOdxa5-e52GkRE?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T21:30:02.435Z",
      "updatedAt": "2023-03-05T21:30:02.435Z"
    },
    {
      "mintAddress": "A7Aq77zxWC1Kz8ykk3obzpHCk9UMDwd5rVK5LZKu75Mb",
      "supply": 1,
      "title": "Entreprenerdz #3373",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.35,
      "escrowPubkey": "3TR3EURLoQeHpqEyPVTXhvm7CwJLPjiZyjt4veHvHxJY",
      "owner": "HyyAAKL5j7THXQY6XfzzzzQUKG7urN8tcRFgFFULsq3d",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "EnHJSmDonipRMEY8yYoE1Ac3ctNEDDi5FiQ3yGWExW5r",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/tpHA0QjFhy_9R4w9i_-czavfyzT-wqhqzFcoOAqMzlU?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "City"
        },
        {
          "trait_type": "Background",
          "value": "Normie"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "White Robe"
        },
        {
          "trait_type": "Desk",
          "value": "Cardboard"
        },
        {
          "trait_type": "Shelf",
          "value": "Malachite"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Open Neon"
        },
        {
          "trait_type": "Desk Prop",
          "value": "GMO"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "TV Remote"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Smoking"
        },
        {
          "trait_type": "Hair",
          "value": "Bowl Auburn"
        },
        {
          "trait_type": "Glasses",
          "value": "VR Headset"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Turquoise Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Marketer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/tpHA0QjFhy_9R4w9i_-czavfyzT-wqhqzFcoOAqMzlU?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T22:51:18.173Z",
      "updatedAt": "2023-03-05T22:51:18.173Z"
    },
    {
      "mintAddress": "3eiV5iF9Mmbm6p6xBMPknDR4M9pzmC7cG794ZR5ycMuV",
      "supply": 1,
      "title": "Entreprenerdz #2026",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.352479388,
      "escrowPubkey": "8p5PpnWxw5GQbau9ntpjUmDLoEMAqDgESBZqTm21gf9o",
      "owner": "DKVJeggxTCcuZCGsRF4aWR28awzXkDwDq17wtTemAdAb",
      "id": "74Ln2UTqfRdEXrjSMgMFKJnCdPr3QLu8jB7w5J8sD7uQ",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/m47xr7VARtHjslXyyCe5G0nPVd0OHFD0nDUVNRI_vHM?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Suburbs"
        },
        {
          "trait_type": "Background",
          "value": "Trader Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "Linked"
        },
        {
          "trait_type": "Desk",
          "value": "Cherry Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Colorful Marble"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Harley Davidson"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Microscope"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Bong"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Meh"
        },
        {
          "trait_type": "Hair",
          "value": "Greasy Long"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Turntables"
        },
        {
          "trait_type": "Profession",
          "value": "Business Developer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/m47xr7VARtHjslXyyCe5G0nPVd0OHFD0nDUVNRI_vHM?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "amm": {
        "poolKey": "EGfQVMKJH9rjKbKa4AWfsn4sGvToJm1xqndZk27nrKA",
        "source": "coral_cube_v2",
        "spotPrice": 2069999999,
        "curveType": "exp",
        "curveDelta": 100,
        "lpFeeBp": 600,
        "poolType": "two_sided",
        "nextSpotPrice": 2219320177.7893753,
        "mmmPoolRank": 6
      },
      "createdAt": "2023-03-05T22:05:37.255Z",
      "updatedAt": "2023-03-05T22:05:37.255Z"
    },
    {
      "mintAddress": "FCGS6Rdw5hkHBAzeCSqkBo7WosFuuLXVr4WCCih4FKb",
      "supply": 1,
      "title": "Entreprenerdz #1008",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.3712,
      "escrowPubkey": "9BcNSbwToXzD9WwyUUkJ9vMXFvD4Fatnhzp9i8ioo1Uy",
      "owner": "perce3N2p5LSHcKS8AUpzqgogvNaiQc1zMapfuKRdBx",
      "id": "4nGoTjVPaipCjraXxdGBJn99v6h8bYULuP11bi89oxk2",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/rVoqSwb0Lx6XMuMAQw7FKH94KwwD4YCFV0R7HIl9kPc?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Mom's Basement"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Black Jacket"
        },
        {
          "trait_type": "Desk",
          "value": "Plum Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Cut Stone"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Stop Sign"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Journal"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "TV Remote"
        },
        {
          "trait_type": "Blemish",
          "value": "Acne"
        },
        {
          "trait_type": "Expression",
          "value": "Suggestive Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Boyish Red"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Turntables"
        },
        {
          "trait_type": "Profession",
          "value": "Artist"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/rVoqSwb0Lx6XMuMAQw7FKH94KwwD4YCFV0R7HIl9kPc?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "amm": {
        "poolKey": "2iEvHywd5pvtcnDmHrZh6wQELhbBZHrGZ6456aWempPU",
        "source": "coral_cube_v2",
        "spotPrice": 2000000000,
        "curveType": "linear",
        "curveDelta": 70000000,
        "lpFeeBp": 400,
        "poolType": "two_sided",
        "nextSpotPrice": 2280000000,
        "mmmPoolRank": 3
      },
      "createdAt": "2023-03-05T19:51:46.208Z",
      "updatedAt": "2023-03-05T19:51:46.208Z"
    },
    {
      "mintAddress": "3CRQx8sC4zq5p6jwusMTNQFxFSBhjyEcZTaWuHSSAoC3",
      "supply": 1,
      "title": "Entreprenerdz #5968",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.376004182,
      "escrowPubkey": "Dk5SEWEEDPpDPnbMj9Cr6PQbuWkcgVfJ9zukU9ca1KoV",
      "owner": "DKVJeggxTCcuZCGsRF4aWR28awzXkDwDq17wtTemAdAb",
      "id": "H2QWTbZXVSwau7rNh62BtWre7jjCtsFD3fsG976q4qA7",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/i14_f0Il7O83Drk9zp2QWAvOh4bSsIxgQvy9Tw9cs8c?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Music Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Dark Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Boobs"
        },
        {
          "trait_type": "Desk",
          "value": "Plum Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Colorful Marble"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Hookah"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Coffee Spill"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Test Tube"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Content"
        },
        {
          "trait_type": "Hair",
          "value": "Bald"
        },
        {
          "trait_type": "Glasses",
          "value": "Nerd"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Rose Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Accountant"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/i14_f0Il7O83Drk9zp2QWAvOh4bSsIxgQvy9Tw9cs8c?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "amm": {
        "poolKey": "EGfQVMKJH9rjKbKa4AWfsn4sGvToJm1xqndZk27nrKA",
        "source": "coral_cube_v2",
        "spotPrice": 2069999999,
        "curveType": "exp",
        "curveDelta": 100,
        "lpFeeBp": 600,
        "poolType": "two_sided",
        "nextSpotPrice": 2241513379.5672693,
        "mmmPoolRank": 7
      },
      "createdAt": "2023-03-05T15:17:20.907Z",
      "updatedAt": "2023-03-05T15:17:20.907Z"
    },
    {
      "mintAddress": "BjyhJNVsBFa1WPBrL4SAavXZkuMjmoABK4vVaQiNbFsP",
      "supply": 1,
      "title": "Entreprenerdz #5087",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.3766,
      "escrowPubkey": "5aPTnTgRwyEFgG1eFmfQW4MrG4pCL4rCgaDzqVqLdEEv",
      "owner": "6p9MtdE6Fau4Q2LrP97WWxrMXMVK9QvsmrVfcMCxuj5D",
      "id": "He2YXRni5K7mUCCPqQF2zdaMtrjCAu3J6wRwHbu81Sfa",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/o0sovigxpuqHu_31ibo1qHBK9gctQGQlmufV9GoaWwg?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Crystals"
        },
        {
          "trait_type": "Background",
          "value": "Anime Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Dark Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Lab Coat"
        },
        {
          "trait_type": "Desk",
          "value": "Gum"
        },
        {
          "trait_type": "Shelf",
          "value": "Geode"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Old Electronics"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Ramen"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Grinder"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Scared"
        },
        {
          "trait_type": "Hair",
          "value": "Thick Black"
        },
        {
          "trait_type": "Glasses",
          "value": "Classic Shades"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "RGB"
        },
        {
          "trait_type": "Profession",
          "value": "Artist"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/o0sovigxpuqHu_31ibo1qHBK9gctQGQlmufV9GoaWwg?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "amm": {
        "poolKey": "AVVymU7mCxW6gb3p9VHB8MVbinLChxVxrheDxuCxeTBz",
        "source": "coral_cube_v2",
        "spotPrice": 1980000000,
        "curveType": "linear",
        "curveDelta": 70000000,
        "lpFeeBp": 200,
        "poolType": "two_sided",
        "nextSpotPrice": 2330000000,
        "mmmPoolRank": 4
      },
      "createdAt": "2023-03-05T17:43:12.263Z",
      "updatedAt": "2023-03-05T17:43:12.263Z"
    },
    {
      "mintAddress": "FvwrqAGpFLpLpFsJ7YUihLk6Y4rdG8V6E1RCQh16c1aq",
      "supply": 1,
      "title": "Entreprenerdz #2561",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.389,
      "escrowPubkey": "DRC2KK7eRA35s99Rqco7zf7MNha4466WSkkSSrpL7JqG",
      "owner": "2GkoX5avH9rig4jp3gtp4UBMmosZKsDtRMWgdH3wixdW",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "6Lxp4crYgqJbeyYBRoFYmKK6Z4pPbsGt9tMdT89p22of",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/0v8uhp8AL7om9FtkXEJbLxWUjP1t_4TFFKzsOLrnvy0?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Suburbs"
        },
        {
          "trait_type": "Background",
          "value": "Anime Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "Denim Jacket"
        },
        {
          "trait_type": "Desk",
          "value": "Weathered"
        },
        {
          "trait_type": "Shelf",
          "value": "Colorful Marble"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Yordans"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Ramen"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Playman"
        },
        {
          "trait_type": "Blemish",
          "value": "Freckles 1"
        },
        {
          "trait_type": "Expression",
          "value": "Content"
        },
        {
          "trait_type": "Hair",
          "value": "Silver Fox"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Wired Black"
        },
        {
          "trait_type": "Profession",
          "value": "Business Developer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/0v8uhp8AL7om9FtkXEJbLxWUjP1t_4TFFKzsOLrnvy0?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T22:35:25.912Z",
      "updatedAt": "2023-03-05T22:35:25.912Z"
    },
    {
      "mintAddress": "8Ankv1CenmAt1sA8coW85mqQCtHXjRt9ws4JMRs63c1t",
      "supply": 1,
      "title": "Entreprenerdz #8366",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.39,
      "escrowPubkey": "CDKWtAvkjLYD17kfpxNs5tyGnrnj3bxJ1j1e4JuLg7ZH",
      "owner": "4rXXnaUwX7isoBhRnrnyPfTnKZjqUGktegjBqCHdPGcX",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "7ZPX5jgdv6oXHoqVpCtbPLTUs4XbSDfHdAqvN8hZ37nM",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/KOcZKwZvTSic5v4ymcHHbeRAmTDLqJGqgyfHlAEKK2Y?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Music Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "Hitman"
        },
        {
          "trait_type": "Desk",
          "value": "Gum"
        },
        {
          "trait_type": "Shelf",
          "value": "Iron Vein"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Old Electronics"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Glasses & Case"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Bong"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Suggestive"
        },
        {
          "trait_type": "Hair",
          "value": "Rock N' Roll Black"
        },
        {
          "trait_type": "Glasses",
          "value": "Nerd"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "RGB"
        },
        {
          "trait_type": "Profession",
          "value": "Marketer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/KOcZKwZvTSic5v4ymcHHbeRAmTDLqJGqgyfHlAEKK2Y?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T18:21:53.740Z",
      "updatedAt": "2023-03-05T18:21:53.740Z"
    },
    {
      "mintAddress": "2yj8BBdxpSXZzb3cJ8pjN8aDEudbvFLah7HR4itiZAik",
      "supply": 1,
      "title": "Entreprenerdz #5445",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.399764224,
      "escrowPubkey": "BiHvdJwDkuENKy7uahLjMngtQX2SBcUqKQoNma8hdreW",
      "owner": "DKVJeggxTCcuZCGsRF4aWR28awzXkDwDq17wtTemAdAb",
      "id": "CwiNv87VpH1dYgWHfSwcZXZQjjnU1XeaxhDKvMqhK7LQ",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/oKY3K48gd1QlJbJ2upZb0jG7KBeTGODcA7X8SuodZ6o?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Tropical"
        },
        {
          "trait_type": "Background",
          "value": "D&D"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Fair"
        },
        {
          "trait_type": "Clothes",
          "value": "Fallout"
        },
        {
          "trait_type": "Desk",
          "value": "Weathered"
        },
        {
          "trait_type": "Shelf",
          "value": "Metal"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Rare Gems"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Glasses & Case"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Moisturiser"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Suggestive"
        },
        {
          "trait_type": "Hair",
          "value": "Rock N' Roll Black"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Classic White"
        },
        {
          "trait_type": "Profession",
          "value": "Trader"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/oKY3K48gd1QlJbJ2upZb0jG7KBeTGODcA7X8SuodZ6o?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "amm": {
        "poolKey": "EGfQVMKJH9rjKbKa4AWfsn4sGvToJm1xqndZk27nrKA",
        "source": "coral_cube_v2",
        "spotPrice": 2069999999,
        "curveType": "exp",
        "curveDelta": 100,
        "lpFeeBp": 600,
        "poolType": "two_sided",
        "nextSpotPrice": 2263928513.3629417,
        "mmmPoolRank": 8
      },
      "createdAt": "2023-03-05T21:47:31.772Z",
      "updatedAt": "2023-03-05T21:47:31.772Z"
    },
    {
      "mintAddress": "2QZBqU391J7AVEUZRVMwC88DranAywdVaJSfAmhfX1e9",
      "supply": 1,
      "title": "Entreprenerdz #3719",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.4,
      "escrowPubkey": "EH4YqStxwNTu1XDML4kSmjwuBK259aJcygLT9HhCTJrq",
      "owner": "3NCSVGy8o5PH1R9eA5FJ3CgNqLe6b1VaKCnai9ujFvCN",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "3EPVD9Fs86DPjHaqmGjdp9WGofgNizQYc41hNiM8ZGbb",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/J6jzpAwWIszAqAZhG8IpFwOnuAXF0AsV30toTOFouUs?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Tropical"
        },
        {
          "trait_type": "Background",
          "value": "Anime Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Medium"
        },
        {
          "trait_type": "Clothes",
          "value": "White Robe"
        },
        {
          "trait_type": "Desk",
          "value": "Plum Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Metal"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Yordans"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Earphones"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Bong"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Horny Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Nerd Middle Part"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "Black"
        },
        {
          "trait_type": "Keyboard",
          "value": "Wired Black"
        },
        {
          "trait_type": "Profession",
          "value": "Degen"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/J6jzpAwWIszAqAZhG8IpFwOnuAXF0AsV30toTOFouUs?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T18:32:59.835Z",
      "updatedAt": "2023-03-05T18:32:59.835Z"
    },
    {
      "mintAddress": "5c2Da5jtgvF7ujK9V8uAgnEqgCiBoqH5prfuhHwRpvLt",
      "supply": 1,
      "title": "Entreprenerdz #1637",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.4,
      "escrowPubkey": "64BNvGdNdHpe5mWefazsj1ECvhywbAQ6ofc4M9AXp8Wh",
      "owner": "5bnVKdk6qrDVW4L4Z6hQtgRZnpfJ4ww7tK7iotY4ntHW",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "FSjraGNYwbKCUzYgh5vHjGdr2cgjUnfcUgjVmYfonbaH",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/QeV3Oif_GS5OIe4VsSsJPjKepFO2Hq-avpdZ7AsinDw?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Mom's Basement"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Fair"
        },
        {
          "trait_type": "Clothes",
          "value": "Fallout"
        },
        {
          "trait_type": "Desk",
          "value": "Oak"
        },
        {
          "trait_type": "Shelf",
          "value": "Scorched"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Model Jet"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Joystick"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Books"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Suggestive"
        },
        {
          "trait_type": "Hair",
          "value": "Newsboy Cap"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Wired Black"
        },
        {
          "trait_type": "Profession",
          "value": "Marketer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/QeV3Oif_GS5OIe4VsSsJPjKepFO2Hq-avpdZ7AsinDw?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T17:56:58.830Z",
      "updatedAt": "2023-03-05T17:56:58.830Z"
    },
    {
      "mintAddress": "89ccdnyKrNeqaQEqh7mSzz1S2ZP42mD8qQuJa6S7Awxe",
      "supply": 1,
      "title": "Entreprenerdz #8978",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.4,
      "escrowPubkey": "22hwuX6tzJZj16mXURtfM3yCmFK9XcL41RXZvuzavfo3",
      "owner": "7wta1bnbcUvXzVnb4iTFaH9efoyDeFUcyBcum9Vjochr",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "2FL25HNe3kZoAsHEf15o57jfgTQPfVFP1jcsGja2m5vy",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/BmTBFzJoNWkpS-zuJn4CLXQcBmyb1CmBKS9eFfLfjiA?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Trash Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Fair"
        },
        {
          "trait_type": "Clothes",
          "value": "Stay Focused"
        },
        {
          "trait_type": "Desk",
          "value": "Oak"
        },
        {
          "trait_type": "Shelf",
          "value": "Geode"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Sparky"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Smartwatch"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Iphone & Airpods"
        },
        {
          "trait_type": "Blemish",
          "value": "Freckles 2"
        },
        {
          "trait_type": "Expression",
          "value": "Suggestive Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Curtain Black"
        },
        {
          "trait_type": "Glasses",
          "value": "Nerd"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Classic White"
        },
        {
          "trait_type": "Profession",
          "value": "Business Developer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/BmTBFzJoNWkpS-zuJn4CLXQcBmyb1CmBKS9eFfLfjiA?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T21:53:43.136Z",
      "updatedAt": "2023-03-05T21:53:43.136Z"
    },
    {
      "mintAddress": "FEaTeDTvTEQkB7GsuXdKUz63WQDMYWHGXahBAkCNq7hD",
      "supply": 1,
      "title": "Entreprenerdz #4788",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.4,
      "escrowPubkey": "2xSGaa1MGQhkdijjjWN8w7jmzDVbALdx7sWvCVJuEtAG",
      "owner": "3bAUhttbpLuSifgQ3qWqQJN64f6j4iepe6mgrWnSREjN",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "B2rkmJf3bx5nNkyjStbj2GVqjgSmpJW3KGtqQGh8VS5q",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/FtJnBGnaUvB2A54YjLlniHGqPoC45VkanIn3FGFKEvs?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "City"
        },
        {
          "trait_type": "Background",
          "value": "Degenformers"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Dark Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "White Robe"
        },
        {
          "trait_type": "Desk",
          "value": "Plum Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Iron Vein"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Medication"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Trophy"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Takeout Trash"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Happy"
        },
        {
          "trait_type": "Hair",
          "value": "Torn Hat"
        },
        {
          "trait_type": "Glasses",
          "value": "Radar Shades"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Snow Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Accountant"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/FtJnBGnaUvB2A54YjLlniHGqPoC45VkanIn3FGFKEvs?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T22:32:05.818Z",
      "updatedAt": "2023-03-05T22:32:05.818Z"
    },
    {
      "mintAddress": "FpLsCmg6CiUprkKo3pLf8uWkT8BFzG4X3TS3LrT5b9mh",
      "supply": 1,
      "title": "Entreprenerdz #7534",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.4,
      "escrowPubkey": "DNrDnN9Na2B7SCF86ym5fUsR82ApDdFFE8hherQdt98b",
      "owner": "8FFdNmtjqYRZmuW2TBFM5gq72N3eHPStJ2U8syHsuUP9",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "G5fZG3NQFSYsyeNRC89HLThU4bEQtQX9Who4bks2Rs46",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/_WZlwjdCNd8akJk8w9Zwf-i2Wm9kGhoHKPtQk56lLTY?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Game Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Medium"
        },
        {
          "trait_type": "Clothes",
          "value": "White Robe"
        },
        {
          "trait_type": "Desk",
          "value": "Weathered"
        },
        {
          "trait_type": "Shelf",
          "value": "Lava Core"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Model Jet"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Water Bottle"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Frog Incense"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Horny Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Rock N' Roll Black"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Turquoise Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Business Developer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/_WZlwjdCNd8akJk8w9Zwf-i2Wm9kGhoHKPtQk56lLTY?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T22:52:22.218Z",
      "updatedAt": "2023-03-05T22:52:22.218Z"
    },
    {
      "mintAddress": "Biv9RiEZw9BLQKZdZdRW985La1q8Hv1BBarx3MxNtEHM",
      "supply": 1,
      "title": "Entreprenerdz #7097",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.41,
      "escrowPubkey": "4xzCzioiEwxyEsRDdhEE5UZXGU4Xg3KSXYX1bDrpKrQR",
      "owner": "9qBY8PpmvvL5xFiLyhts1AUUUcEzRRsgKAmPqJVk7bpH",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "5T68nc44HBe1eD3N8bKpERUJSkV6M2BRy22RDi527sb2",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/exKHMoNbnwqxs1cDf-y0rmD4IVns9f4GMjzrX31cEEQ?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "City"
        },
        {
          "trait_type": "Background",
          "value": "Normie"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "Stay Focused"
        },
        {
          "trait_type": "Desk",
          "value": "Oak"
        },
        {
          "trait_type": "Shelf",
          "value": "Colorful Marble"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Record Player"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Floating Moon"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Moisturiser"
        },
        {
          "trait_type": "Blemish",
          "value": "Freckles 2"
        },
        {
          "trait_type": "Expression",
          "value": "Delirious"
        },
        {
          "trait_type": "Hair",
          "value": "Rock N' Roll Black"
        },
        {
          "trait_type": "Glasses",
          "value": "Radar Shades"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Classic White"
        },
        {
          "trait_type": "Profession",
          "value": "Business Developer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/exKHMoNbnwqxs1cDf-y0rmD4IVns9f4GMjzrX31cEEQ?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T18:05:10.895Z",
      "updatedAt": "2023-03-05T18:05:10.895Z"
    },
    {
      "mintAddress": "AkriggSneG9NHMUq32fHHgdqMv5NZg7ZX1NsUXniFYX5",
      "supply": 1,
      "title": "Entreprenerdz #8100",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.42069,
      "escrowPubkey": "2ghnkYdLyQHSct7a71SJksb9hS9omoy3g7Rw8Zv1WGRB",
      "owner": "Enochf5h8U4GGrCyepYoJ5nwcy8kwNmNuzBdX1yb9Kwa",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "9ep2LfUMSs5H9BtAN4rxgkE28uhyhPZKA1oLNzvzhvEL",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/wND46s1O8-fQ4QWQud2xaiVWKRsd-q7pLkzXtvQZ7nw?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Castle"
        },
        {
          "trait_type": "Background",
          "value": "Penthouse"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Medium"
        },
        {
          "trait_type": "Clothes",
          "value": "Agent S"
        },
        {
          "trait_type": "Desk",
          "value": "Gum"
        },
        {
          "trait_type": "Shelf",
          "value": "Mosaic"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Troop"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Calculator"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "TV Remote"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Strained"
        },
        {
          "trait_type": "Hair",
          "value": "Thick Brown"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Turntables"
        },
        {
          "trait_type": "Profession",
          "value": "Code Wizard"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/wND46s1O8-fQ4QWQud2xaiVWKRsd-q7pLkzXtvQZ7nw?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T22:48:25.818Z",
      "updatedAt": "2023-03-05T22:48:25.818Z"
    },
    {
      "mintAddress": "jUAsHp3f6t9ARYzJzBBMQFWKaP7HwitikkD1HappCBN",
      "supply": 1,
      "title": "Entreprenerdz #9621",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.423761866,
      "escrowPubkey": "E3Ez5GitVcR9NyhwKDDntVuWy2yREjRCNAvsm9dLjRdX",
      "owner": "DKVJeggxTCcuZCGsRF4aWR28awzXkDwDq17wtTemAdAb",
      "id": "AdQVHHwpeXJniwcn13GQVmdvxbMAPhTPdDY9tdTQXvxj",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/uiprasCiGnKaGmHJ8X1FRWaZycA5jgw5NwnD3Kz-Ugw?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Crystals"
        },
        {
          "trait_type": "Background",
          "value": "Trader Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Medium"
        },
        {
          "trait_type": "Clothes",
          "value": "Torn Cloak"
        },
        {
          "trait_type": "Desk",
          "value": "Weathered"
        },
        {
          "trait_type": "Shelf",
          "value": "Zebra"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Harley Davidson"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Ramen"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Books"
        },
        {
          "trait_type": "Blemish",
          "value": "Acne"
        },
        {
          "trait_type": "Expression",
          "value": "Shook"
        },
        {
          "trait_type": "Hair",
          "value": "Thick Brown"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Tablet"
        },
        {
          "trait_type": "Profession",
          "value": "Artist"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/uiprasCiGnKaGmHJ8X1FRWaZycA5jgw5NwnD3Kz-Ugw?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "amm": {
        "poolKey": "EGfQVMKJH9rjKbKa4AWfsn4sGvToJm1xqndZk27nrKA",
        "source": "coral_cube_v2",
        "spotPrice": 2069999999,
        "curveType": "exp",
        "curveDelta": 100,
        "lpFeeBp": 600,
        "poolType": "two_sided",
        "nextSpotPrice": 2286567798.496571,
        "mmmPoolRank": 9
      },
      "createdAt": "2023-03-05T17:41:31.114Z",
      "updatedAt": "2023-03-05T17:41:31.114Z"
    },
    {
      "mintAddress": "9QAxuopaw8GewtuHskPrx9qmCcyTDQipSU6Uth8ZJqLG",
      "supply": 1,
      "title": "Entreprenerdz #1416",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.444,
      "escrowPubkey": "DpL9oeBbeuAGWUnCec2sG7Ko2SoA7JfCPX3ZzSBLkcSE",
      "owner": "perce3N2p5LSHcKS8AUpzqgogvNaiQc1zMapfuKRdBx",
      "id": "6kfDtnJ98FbmwMTjWrfPZU9BZS9idKkifg2UFUj9JXmG",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/JAaVnLyiC-CpuGbnMIb4gqcXh3kkugYJ72tHTxxfOv0?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Game Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "Torn Shirt"
        },
        {
          "trait_type": "Desk",
          "value": "Oak"
        },
        {
          "trait_type": "Shelf",
          "value": "Metal"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Katana"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Living Plant"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Space Shuttle"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Suggestive"
        },
        {
          "trait_type": "Hair",
          "value": "Torn Hat"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Compact Black"
        },
        {
          "trait_type": "Profession",
          "value": "Entrepreneur"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/JAaVnLyiC-CpuGbnMIb4gqcXh3kkugYJ72tHTxxfOv0?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "amm": {
        "poolKey": "2iEvHywd5pvtcnDmHrZh6wQELhbBZHrGZ6456aWempPU",
        "source": "coral_cube_v2",
        "spotPrice": 2000000000,
        "curveType": "linear",
        "curveDelta": 70000000,
        "lpFeeBp": 400,
        "poolType": "two_sided",
        "nextSpotPrice": 2350000000,
        "mmmPoolRank": 4
      },
      "createdAt": "2023-03-05T12:47:17.806Z",
      "updatedAt": "2023-03-05T12:47:17.806Z"
    },
    {
      "mintAddress": "Ffowgy2oKvmfdiUqkXtu6W8Tz1r9JprEu8Tu3ekZTVie",
      "supply": 1,
      "title": "Entreprenerdz #749",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.448,
      "escrowPubkey": "FG21hp8DrL1hSXYH1c45wozQCEJmngR1CaRz7CH9MT7M",
      "owner": "6p9MtdE6Fau4Q2LrP97WWxrMXMVK9QvsmrVfcMCxuj5D",
      "id": "G3ZH9zjTPtFjqTPGAPReCjCho4vj5mRDaoX9jhFPUcM2",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/837fKvhTlUgI7-IvmKoUEdSYMAdP-KJgFDQfAxW5dsc?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Trash Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Fair"
        },
        {
          "trait_type": "Clothes",
          "value": "Beatz by Nerdz"
        },
        {
          "trait_type": "Desk",
          "value": "Weathered"
        },
        {
          "trait_type": "Shelf",
          "value": "Geode"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Saber Blue"
        },
        {
          "trait_type": "Desk Prop",
          "value": "VR Controllers"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Light Therapy Lamp"
        },
        {
          "trait_type": "Blemish",
          "value": "Scar"
        },
        {
          "trait_type": "Expression",
          "value": "Suggestive"
        },
        {
          "trait_type": "Hair",
          "value": "Spike"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Turntables"
        },
        {
          "trait_type": "Profession",
          "value": "Artist"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/837fKvhTlUgI7-IvmKoUEdSYMAdP-KJgFDQfAxW5dsc?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "amm": {
        "poolKey": "AVVymU7mCxW6gb3p9VHB8MVbinLChxVxrheDxuCxeTBz",
        "source": "coral_cube_v2",
        "spotPrice": 1980000000,
        "curveType": "linear",
        "curveDelta": 70000000,
        "lpFeeBp": 200,
        "poolType": "two_sided",
        "nextSpotPrice": 2400000000,
        "mmmPoolRank": 5
      },
      "createdAt": "2023-03-05T19:44:03.635Z",
      "updatedAt": "2023-03-05T19:44:03.635Z"
    },
    {
      "mintAddress": "8PK92MS4ZaRFvCauBPRRYBHkzPSQKqaocD1Y2qYW5Fsk",
      "supply": 1,
      "title": "Entreprenerdz #6705",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.45,
      "escrowPubkey": "96Khc5y3GiiW7NF1Sgvm85ppp6493NjjWjiqdz97ujy8",
      "owner": "GniFadS775QCvypSjYpHiLTTuX9G7gp1Q6UDs3irX2wp",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "3rbaABDMfHkqu2c71K3Ki4iiq8jZqNbH1T4ZyyFskDbF",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/zNYBcJyZ8TA03cMFj6Bu3kLBwlcldgZ19SH6lq9OFy8?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Music Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "Fallout"
        },
        {
          "trait_type": "Desk",
          "value": "Metal"
        },
        {
          "trait_type": "Shelf",
          "value": "Metal"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Scythe"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Ashtray"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Desk Mic"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Smoking"
        },
        {
          "trait_type": "Hair",
          "value": "Curtain Black"
        },
        {
          "trait_type": "Glasses",
          "value": "Harry"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Rose Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Marketer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/zNYBcJyZ8TA03cMFj6Bu3kLBwlcldgZ19SH6lq9OFy8?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T20:05:17.329Z",
      "updatedAt": "2023-03-05T20:05:17.329Z"
    },
    {
      "mintAddress": "47raXqycZKRw7iAznm1af3xs5rdoFybCPNgHF1cdzVXR",
      "supply": 1,
      "title": "Entreprenerdz #8032",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.45,
      "escrowPubkey": "58NLB8kszLFKSDvq1wbczsfCvTmioVoF641MLHEwyrC9",
      "owner": "CeXR74x6dbvUNucXWzY5jKtAFQ2zbLyxtJfxd6v1YcEn",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "ER5PuRqmTxWW7mpdeA3G6A7h9KaMjq5gLtY3K7YhxvVU",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/OgLIBU3e4URSc876A49m5oxeUd1PZzQ1dEod3nr_QWE?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Mom's Basement"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Torn Shirt"
        },
        {
          "trait_type": "Desk",
          "value": "Oak"
        },
        {
          "trait_type": "Shelf",
          "value": "Metal"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Open Neon"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Quill & Ink"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Newton's Cradle Pendulum"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Smoking Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Rock N' Roll Golden"
        },
        {
          "trait_type": "Glasses",
          "value": "Nerd"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Wired Black"
        },
        {
          "trait_type": "Profession",
          "value": "Marketer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/OgLIBU3e4URSc876A49m5oxeUd1PZzQ1dEod3nr_QWE?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T20:26:22.024Z",
      "updatedAt": "2023-03-05T20:26:22.024Z"
    },
    {
      "mintAddress": "2xbWZ38ZciUvdVEDy8fKdmPFDw8mLjWyLDhJm6v9a321",
      "supply": 1,
      "title": "Entreprenerdz #1026",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.45,
      "escrowPubkey": "GX4Wyy6HJmiLKDEQaUvhHjdb24j4UJPAbn9wjMsyeXpD",
      "owner": "6cptBVvc4zWpfj7vfcwcpufKwXnpFnW3VhEEL7t4tGAL",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "2s5LAtq8oCryUxJdzbh6TE98hnsNjKdDE3ACfMgxoND9",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/U8pjTfXCJrehaM6NnyRx_l7H9U_cnNcrtUBPFszZqsI?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Crystals"
        },
        {
          "trait_type": "Background",
          "value": "Normie"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Olive"
        },
        {
          "trait_type": "Clothes",
          "value": "NeRDy"
        },
        {
          "trait_type": "Desk",
          "value": "Oak"
        },
        {
          "trait_type": "Shelf",
          "value": "Wood"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Saber Red"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Trophy"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Books"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Angry"
        },
        {
          "trait_type": "Hair",
          "value": "Bowl Golden"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "Golden"
        },
        {
          "trait_type": "Keyboard",
          "value": "Wired Black"
        },
        {
          "trait_type": "Profession",
          "value": "Entrepreneur"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/U8pjTfXCJrehaM6NnyRx_l7H9U_cnNcrtUBPFszZqsI?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T21:38:31.567Z",
      "updatedAt": "2023-03-05T21:38:31.567Z"
    },
    {
      "mintAddress": "Gd2KznqoTWV5tQeGZjV7CvX5C3SYF1m4LWpHqAB5U1d4",
      "supply": 1,
      "title": "Entreprenerdz #6811",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.45,
      "escrowPubkey": "GFLgTe24LFK1SkRnT9JNAh2CPaBaKbA5PYdu8xsctqth",
      "owner": "ATFghSXEJVitV19PUqDMr2TKhq25iUd8fvNstHHX48tX",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "ED54Xgd7uox2GYKozMjiZ7FfedKfS3JtUHSLwY6AqiS1",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/i_FlzxKXTNCaDkJG7E4aL913WecNcBEQUsRHUr24TWY?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Trash Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Dark Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Jersey"
        },
        {
          "trait_type": "Desk",
          "value": "Gum"
        },
        {
          "trait_type": "Shelf",
          "value": "Metal"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Hammer"
        },
        {
          "trait_type": "Desk Prop",
          "value": "GigaPower"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Speaker"
        },
        {
          "trait_type": "Blemish",
          "value": "Blush"
        },
        {
          "trait_type": "Expression",
          "value": "Meh"
        },
        {
          "trait_type": "Hair",
          "value": "Bowl Golden"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Switch"
        },
        {
          "trait_type": "Profession",
          "value": "Marketer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/i_FlzxKXTNCaDkJG7E4aL913WecNcBEQUsRHUr24TWY?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T22:15:17.271Z",
      "updatedAt": "2023-03-05T22:15:17.271Z"
    },
    {
      "mintAddress": "8xswageQsmkV6Rw2Cj1qqTJ2F3DVUz5W7PJn3Ar9Lrkd",
      "supply": 1,
      "title": "Entreprenerdz #7802",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.48,
      "escrowPubkey": "6h97ppyiv8RSaTTJ17ivK9ZJrpyZLWLmnqajYZbN5fVK",
      "owner": "BgKTdUxdC3jiTgxHs57ZxkMrTPN8RuoiBBz2zST1LJvp",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "H5x5FVzLHAqgdh8HKB6qwTW5yzT6k2WAdnoQTqaGdvzJ",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/TQPff1Dn_vy1JpJHPd2e_6ZQrFNq-2WS_FtKf-Kv87Q?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Tropical"
        },
        {
          "trait_type": "Background",
          "value": "Cozy Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Medium"
        },
        {
          "trait_type": "Clothes",
          "value": "Jock"
        },
        {
          "trait_type": "Desk",
          "value": "Oak"
        },
        {
          "trait_type": "Shelf",
          "value": "Cut Stone"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Saber Blue"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Floating Moon"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Bong"
        },
        {
          "trait_type": "Blemish",
          "value": "Acne"
        },
        {
          "trait_type": "Expression",
          "value": "Suggestive Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Nerd Middle Part"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Snow Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Code Wizard"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/TQPff1Dn_vy1JpJHPd2e_6ZQrFNq-2WS_FtKf-Kv87Q?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T20:58:14.813Z",
      "updatedAt": "2023-03-05T20:58:14.813Z"
    },
    {
      "mintAddress": "4dDGjUEZfTWqvjobeKeTEwMHtakrCjk5K9PhpEfaZTnn",
      "supply": 1,
      "title": "Entreprenerdz #4392",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.487,
      "escrowPubkey": "ErtUJKTpVQ7n8VXuCvuQ8YKGed6Nz1pCJHE47z61tBVT",
      "owner": "2GkoX5avH9rig4jp3gtp4UBMmosZKsDtRMWgdH3wixdW",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "8SeWNdNg4biT7guazmFzNAXjzBu92fz4gokeZEjEK3Xz",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/SRDJ1G2nk-iJBAuG65GyuzC8DX4RQFpkiU8cWDRiA8w?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Black Hole"
        },
        {
          "trait_type": "Background",
          "value": "Trader Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Dark Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Flannel"
        },
        {
          "trait_type": "Desk",
          "value": "Gum"
        },
        {
          "trait_type": "Shelf",
          "value": "Wood"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Troop"
        },
        {
          "trait_type": "Desk Prop",
          "value": "GigaPower"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Drinking Bird"
        },
        {
          "trait_type": "Blemish",
          "value": "Blush"
        },
        {
          "trait_type": "Expression",
          "value": "Wicked"
        },
        {
          "trait_type": "Hair",
          "value": "Nerd Side Part"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Classic White"
        },
        {
          "trait_type": "Profession",
          "value": "Trader"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/SRDJ1G2nk-iJBAuG65GyuzC8DX4RQFpkiU8cWDRiA8w?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T22:35:25.907Z",
      "updatedAt": "2023-03-05T22:35:25.907Z"
    },
    {
      "mintAddress": "GJr2aKQimKfEXLdGLuJm3JHJtTHpPQJhUz36HetxzjU8",
      "supply": 1,
      "title": "Entreprenerdz #9951",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.489,
      "escrowPubkey": "E9PFKurPeVsKNmCDrKVJaU3n78Xca6CHceUjzX4V41gu",
      "owner": "CPM54uLfLWdu7ebpU7iFJcaoHr7Y3qs6ND55WynMKv38",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "D1PDY5Xf2afKxMUc1WcoQHEzbufkGingvxsTERZ1RJxp",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/fSHnn2HqejVmIoiMFeGAd0Qigh-U_H_yEWEDqSXCowQ?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Crystals"
        },
        {
          "trait_type": "Background",
          "value": "Anime Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Fair"
        },
        {
          "trait_type": "Clothes",
          "value": "Boobs"
        },
        {
          "trait_type": "Desk",
          "value": "Cardboard"
        },
        {
          "trait_type": "Shelf",
          "value": "Metal"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Troop"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Film Camera"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Takeout Trash"
        },
        {
          "trait_type": "Blemish",
          "value": "Freckles 2"
        },
        {
          "trait_type": "Expression",
          "value": "Meh Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Dreads"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Wired Black"
        },
        {
          "trait_type": "Profession",
          "value": "Artist"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/fSHnn2HqejVmIoiMFeGAd0Qigh-U_H_yEWEDqSXCowQ?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T19:23:54.258Z",
      "updatedAt": "2023-03-05T19:23:54.258Z"
    },
    {
      "mintAddress": "H6Yb3K7ZP66Ub8meb5BiNLb9kv9SAy8BPJYz6N2MQE8d",
      "supply": 1,
      "title": "Entreprenerdz #6397",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.49,
      "escrowPubkey": "3j7VmtgvwS1qHhDD6YquQHV2HQpL8d8Nynkcbe11qpFr",
      "owner": "GGi5SgSrMTFFNUocXPAeZK1YodY7TAXc2xxW8saAmSWf",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "7xYzR3ymVt29d6ui2KZ7uK9GwJpymyRa8Gxd5G1feSnf",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/L0y30GHYDodnKwTnOyacOyftw1znz0zP98x4QfkUuOw?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Space"
        },
        {
          "trait_type": "Background",
          "value": "Cozy Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Dark Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Jedi Master"
        },
        {
          "trait_type": "Desk",
          "value": "Gum"
        },
        {
          "trait_type": "Shelf",
          "value": "Pebble"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Plant Paradise"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Film Camera"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Moisturiser"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Drunk Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Boyish Red"
        },
        {
          "trait_type": "Glasses",
          "value": "Broken Nerd"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Compact Black"
        },
        {
          "trait_type": "Profession",
          "value": "Entrepreneur"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/L0y30GHYDodnKwTnOyacOyftw1znz0zP98x4QfkUuOw?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T18:26:14.896Z",
      "updatedAt": "2023-03-05T18:26:14.896Z"
    },
    {
      "mintAddress": "9deenGUntHJCbBZNXw4VdA9uMJdGyAxuzAbKKQo98jKT",
      "supply": 1,
      "title": "Entreprenerdz #3406",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.49,
      "escrowPubkey": "AcmRJApBgRWny4ZkddFubnGGkt89b1TcjoEqsPA3MSdz",
      "owner": "HhRMJPLAKeo2aUuScvEwNGuMJSwsyMiAgKpiAhn7qSgy",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "A5WzgNAJrbQ4NsLXRhX74WHWgwXfPhFpbDqMVA7Jrzji",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/nixDquvY586r1h5GRHDbmj4L_tjbuZM5Oyj6MqMYd7M?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Suburbs"
        },
        {
          "trait_type": "Background",
          "value": "Cozy Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Dark Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Health"
        },
        {
          "trait_type": "Desk",
          "value": "Plum Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Geode"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Books"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Calculator"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Speaker"
        },
        {
          "trait_type": "Blemish",
          "value": "Freckles 2"
        },
        {
          "trait_type": "Expression",
          "value": "Happy"
        },
        {
          "trait_type": "Hair",
          "value": "Cropped Afro"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Compact Black"
        },
        {
          "trait_type": "Profession",
          "value": "Trader"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/nixDquvY586r1h5GRHDbmj4L_tjbuZM5Oyj6MqMYd7M?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T20:31:07.440Z",
      "updatedAt": "2023-03-05T20:31:07.440Z"
    },
    {
      "mintAddress": "2BCJjMZMCCiiyvg1d7b5y2MoUS74RaAoXw3m9g1THFDE",
      "supply": 1,
      "title": "Entreprenerdz #4625",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.49,
      "escrowPubkey": "8LiymPMkmcG75jGqkQf3eQRdS42d9TQPaV6hd5GxKbhX",
      "owner": "CpNuMAiREWJBUBRwbSUNg6R5QTf8QNoH3Y8T7y7eqVGm",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "BWrFnFnz5Gmvp9aWVcVn4pW67f3NbNWJQjXHZS94pXnD",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/EHMtZteXuP9GOwvcWdn_yVRZ1DRU4X9RwMPFTve2DJQ?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "City"
        },
        {
          "trait_type": "Background",
          "value": "Cozy Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Dark Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Band Tee"
        },
        {
          "trait_type": "Desk",
          "value": "Plum Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Ocean Sound"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Record Player"
        },
        {
          "trait_type": "Desk Prop",
          "value": "DSLR Camera"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Takeout Trash"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Sheepish"
        },
        {
          "trait_type": "Hair",
          "value": "Cropped Afro"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Compact Black"
        },
        {
          "trait_type": "Profession",
          "value": "Code Wizard"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/EHMtZteXuP9GOwvcWdn_yVRZ1DRU4X9RwMPFTve2DJQ?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T20:36:24.190Z",
      "updatedAt": "2023-03-05T20:36:24.190Z"
    },
    {
      "mintAddress": "H7wmKHRgmuzY6y7M9dn5WHG6yfqVZnRueqhyu5cyBoDX",
      "supply": 1,
      "title": "Entreprenerdz #9943",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.49,
      "escrowPubkey": "8PwFCRTvcBgAoLRwiMK6UTmzz4DzzmDvYQ9RFcEyin8D",
      "owner": "5RoLdfajwqnU7Jm9D13mkRMiboYTmDAwUciPs88oDEvd",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "CQ7cjbDUeAPmgX8tqcZNdNEB9ZCncmZSGpYpcLU3EeQ8",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/u8IMqGSEB_r4s-ylwgwZ-Nq5NM7GQAp2SluuvfTSxdA?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Trash Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Fair"
        },
        {
          "trait_type": "Clothes",
          "value": "Boxing Robe"
        },
        {
          "trait_type": "Desk",
          "value": "Gum"
        },
        {
          "trait_type": "Shelf",
          "value": "Wood"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Old Electronics"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Beer Bottle"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Iphone & Airpods"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Delirious"
        },
        {
          "trait_type": "Hair",
          "value": "Buzz Cut"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Compact White"
        },
        {
          "trait_type": "Profession",
          "value": "Marketer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/u8IMqGSEB_r4s-ylwgwZ-Nq5NM7GQAp2SluuvfTSxdA?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T22:12:59.800Z",
      "updatedAt": "2023-03-05T22:12:59.800Z"
    },
    {
      "mintAddress": "7i2o87BTJANC21Yn84o8CwpUPskZXLAva7VnhomMKd4W",
      "supply": 1,
      "title": "Entreprenerdz #6884",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.49888,
      "escrowPubkey": "9b2oyPmwgwbS3Sf7gSRp63dU1Zv1keCph8AcLBbGhU7U",
      "owner": "9fQWsGSTLirs9ujehTTqVdsYqttHUuMaSyXWegLkUksk",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "CTrcUix6qrvLfvZPod6CA6ga34d7suk8u79G4PvjxGDU",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/t4loq4_kMXCKWm3lrGdY1L5ZLg-5Gs4wgSfxbl37PAY?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Portal"
        },
        {
          "trait_type": "Background",
          "value": "Penthouse"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Fair"
        },
        {
          "trait_type": "Clothes",
          "value": "Health"
        },
        {
          "trait_type": "Desk",
          "value": "Plum Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Colorful Marble"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Sparky"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Coffee"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Grinder"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Content"
        },
        {
          "trait_type": "Hair",
          "value": "Newsboy Cap"
        },
        {
          "trait_type": "Glasses",
          "value": "Harry"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Wired Black"
        },
        {
          "trait_type": "Profession",
          "value": "Artist"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/t4loq4_kMXCKWm3lrGdY1L5ZLg-5Gs4wgSfxbl37PAY?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T17:33:53.807Z",
      "updatedAt": "2023-03-05T17:33:53.807Z"
    },
    {
      "mintAddress": "2PdHgRG51W3wCNUTcAfhWCFxVDP2itgwFuGcznzLVH5D",
      "supply": 1,
      "title": "Entreprenerdz #2481",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.5,
      "escrowPubkey": "3LMn2mPEGfwPqa7d2FDbJbTZybwD3Z1gXyUyMToQpTat",
      "owner": "3sVLi3hXpnweEPcAqT18ruXVEM8Lg8wJpiaaFYdCVTwf",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "2Mbj8tELNj74BnKjZw7zCN4ZTynQXyW3ar6CZvsFF8Lf",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/hK00GIXdgL-5FInjOnBfPNGzQRyguXRiPfYhvJdZDS0?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "Tropical"
        },
        {
          "trait_type": "Background",
          "value": "Cozy Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Overalls"
        },
        {
          "trait_type": "Desk",
          "value": "Cherry Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Cut Stone"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Medication"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Journal"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Dice"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Drunk Facial Hair"
        },
        {
          "trait_type": "Hair",
          "value": "Mullet Brown"
        },
        {
          "trait_type": "Glasses",
          "value": "Broken Nerd"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Snow Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Artist"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/hK00GIXdgL-5FInjOnBfPNGzQRyguXRiPfYhvJdZDS0?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T17:23:28.616Z",
      "updatedAt": "2023-03-05T17:23:28.616Z"
    },
    {
      "mintAddress": "Bz7S21MSpMPhAWMvb4NANadxy9dW5k2GLPFdGrWHUmVn",
      "supply": 1,
      "title": "Entreprenerdz #1466",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.5,
      "escrowPubkey": "HpCdkcEEUbbXCfuhbhVPqMz3de1A8vdmUJQUmDLVdwfY",
      "owner": "5iMXYYNLbLoN86dHiajRqw7ofFFFVMH3RGhAAneKMx4b",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "HLD23YxWrhnsyfr5etCZDhFBMJ5TW1nt4bZAuW7JPmW6",
        "expiry": -1
      },
      "id": "3hjjgA9rr3p6QD6Gz7YiPoU8Rsy7Sc7opWRkw5oZT6g9",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/g79QHzB0TKOBSKO6bdo-g3dQhZiOF0HKW2Xe1ZoHs0M?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Game Room"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Brown"
        },
        {
          "trait_type": "Clothes",
          "value": "Torn Shirt"
        },
        {
          "trait_type": "Desk",
          "value": "Plum Wood"
        },
        {
          "trait_type": "Shelf",
          "value": "Ocean Sound"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Medication"
        },
        {
          "trait_type": "Desk Prop",
          "value": "GigaPower"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Tesseract"
        },
        {
          "trait_type": "Blemish",
          "value": "Acne"
        },
        {
          "trait_type": "Expression",
          "value": "Strained"
        },
        {
          "trait_type": "Hair",
          "value": "Undercut"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Tablet"
        },
        {
          "trait_type": "Profession",
          "value": "Artist"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/g79QHzB0TKOBSKO6bdo-g3dQhZiOF0HKW2Xe1ZoHs0M?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "creators": [
          {
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
            "share": 100
          }
        ],
        "category": "image"
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T18:03:05.098Z",
      "updatedAt": "2023-03-05T18:03:05.098Z"
    },
    {
      "mintAddress": "6doNBEQo7XhgddvwWxq9vX3byRaM6hcqtwcGAFwapdtA",
      "supply": 1,
      "title": "Entreprenerdz #124",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.5,
      "escrowPubkey": "BCkFRs7vsGecPfQ7W4a2ohm3R2SydQzhJg6SyNksf31t",
      "owner": "A73PhWUDtB6EuDiAHocwmAjQm3s8PyxtnfmBvHPskcQC",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "5AGpmp8rD5Aeo6pPMH6fXc5tY4ogbpcfxUJ34YWugzE1",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/FwOdCnD5za1bx8dnvMKr2d7tpWvXfbgM1DarSlamwWs?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Mom's Basement"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Fair"
        },
        {
          "trait_type": "Clothes",
          "value": "Giga Polo"
        },
        {
          "trait_type": "Desk",
          "value": "Gum"
        },
        {
          "trait_type": "Shelf",
          "value": "Ocean Sound"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Boombox"
        },
        {
          "trait_type": "Desk Prop",
          "value": "GMO"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Frog Incense"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Happy"
        },
        {
          "trait_type": "Hair",
          "value": "Nerd Middle Part"
        },
        {
          "trait_type": "Glasses",
          "value": "None"
        },
        {
          "trait_type": "Beard",
          "value": "Black"
        },
        {
          "trait_type": "Keyboard",
          "value": "Turquoise Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Business Developer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/FwOdCnD5za1bx8dnvMKr2d7tpWvXfbgM1DarSlamwWs?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T17:46:40.098Z",
      "updatedAt": "2023-03-05T17:46:40.098Z"
    },
    {
      "mintAddress": "38g1jJkVEaH6zmQGKoHudyU2XSXuqe2NKm76YgPqv9cM",
      "supply": 1,
      "title": "Entreprenerdz #251",
      "content": "We are the Entreprenerdz eating glass & staring into the abyss",
      "primarySaleHappened": True,
      "updateAuthority": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
      "onChainCollection": {
        "key": "6wx1Qe8Cb4dfgkucA7NdB6THQAdn3usNg35gFYPKkdJd",
        "verified": 1,
        "data": {
          "name": "Entreprenerdz",
          "image": "https://arweave.net/OYmu2Dl7e5WdvHVftJlEXGnfpQj5lFiPanCmjsTcttk",
          "description": "We are the Entreprenerdz eating glass & staring into the abyss"
        }
      },
      "sellerFeeBasisPoints": 0,
      "creators": [
        {
          "address": "Cdo2dGRZ9avv2n397X2R1yy41mn32PpjqfpJAfawsVCD",
          "verified": 1,
          "share": 0
        },
        {
          "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u",
          "verified": 0,
          "share": 100
        }
      ],
      "price": 2.5,
      "escrowPubkey": "9RgUvq73fJS6rUd9U7CCUBL6BvWcgBeT2HV1u5gfeu7B",
      "owner": "JVG5EhtMK3jaawNJhgirBsfCdXwJhtFrupMtoeviNqs",
      "v2": {
        "auctionHouseKey": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "sellerReferral": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "expiry": -1
      },
      "id": "3ntiqBAPyZtpiiffCUMPSCsTPPJBugTSuPD1fLVeGVRG",
      "tokenDelegateValid": False,
      "isFrozen": False,
      "tokenStandard": 1,
      "img": "https://arweave.net/Bhu-sfC2TrOV0bto4b2wPAuphsc8BVY5TFNym19P9i4?ext=jpg",
      "attributes": [
        {
          "trait_type": "Window",
          "value": "None"
        },
        {
          "trait_type": "Background",
          "value": "Mom's Basement"
        },
        {
          "trait_type": "Skin Tone",
          "value": "Medium"
        },
        {
          "trait_type": "Clothes",
          "value": "Touch Grass"
        },
        {
          "trait_type": "Desk",
          "value": "Oak"
        },
        {
          "trait_type": "Shelf",
          "value": "Malachite"
        },
        {
          "trait_type": "Shelf Prop",
          "value": "Open Neon"
        },
        {
          "trait_type": "Desk Prop",
          "value": "Megaman"
        },
        {
          "trait_type": "Desk Prop 2",
          "value": "Light Therapy Lamp"
        },
        {
          "trait_type": "Blemish",
          "value": "None"
        },
        {
          "trait_type": "Expression",
          "value": "Satisfied"
        },
        {
          "trait_type": "Hair",
          "value": "Newsboy Cap"
        },
        {
          "trait_type": "Glasses",
          "value": "Nerd"
        },
        {
          "trait_type": "Beard",
          "value": "None"
        },
        {
          "trait_type": "Keyboard",
          "value": "Snow Slim"
        },
        {
          "trait_type": "Profession",
          "value": "Business Developer"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": "https://arweave.net/Bhu-sfC2TrOV0bto4b2wPAuphsc8BVY5TFNym19P9i4?ext=jpg",
            "type": "image/jpeg"
          }
        ],
        "category": "image",
        "creators": [
          {
            "share": 100,
            "address": "D2VNiG9RWVpeLCgQbWM5AKgFcuRtp2gnXjenKCeCFx5u"
          }
        ]
      },
      "propertyCategory": "image",
      "externalURL": "https://linktr.ee/gigadao",
      "collectionName": "entreprenerdz",
      "collectionTitle": "Entreprenerdz",
      "isTradeable": True,
      "rarity": {
        
      },
      "createdAt": "2023-03-05T17:24:23.828Z",
      "updatedAt": "2023-03-05T17:24:23.828Z"
    }
  ]
}
    return dict(results=data.get("results")[:amount])