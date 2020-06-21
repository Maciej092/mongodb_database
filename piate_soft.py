result = client['db-aggregations']['air_routes'].aggregate([
    {
        '$match': {
            'src_airport': 'PSA'
        }
    }, {
        '$graphLookup': {
            'from': 'air_routes',
            'startWith': '$src_airport',
            'connectFromField': 'dst_airport',
            'connectToField': 'src_airport',
            'maxDepth': 2,
            'depthField': 'changes',
            'as': 'change'
        }
    }, {
        '$addFields': {
            'change': {
                '$filter': {
                    'input': '$change',
                    'cond': {
                        '$eq': [
                            '$$this.changes', 2
                        ]
                    }
                }
            }
        }
    }
])