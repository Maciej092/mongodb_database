from pymongo import MongoClient


url = 'mongodb+srv://zabd2020:aggregations@db2020-aggregations-2sawx.mongodb.net/admin?authSource=admin&replicaSet=db2020-aggregations-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true'


def get_connection():
    return MongoClient(url)


def print_results(result, lim):
    cnt = 0
    for item in result:
        print(item,'\n')
        cnt += 1
        if cnt == lim:
            break


def zad_1():
    with get_connection() as client:
        result = client['db-aggregations']['movies'].aggregate([
            {'$match': {'$and': [{'languages': 'English'}, {'languages': 'German'}]}},
            {'$project': {'_id': 0, 'title': 1,'imdb.rating': 1}}])
        print_results(result)


def zad_2():
    with get_connection() as client:
        result = client['db-aggregations']['movies'].aggregate([
            {"$match": {"year": {"$gt": 1960},
                        "imdb.rating": {"$gt": 5},
                        "directors": {"$exists": "true"},
                        "cast": {"$exists": "true"}}
             },
            {"$project": {"_id": 0,
                          "title": "$title",
                          "rating": "$imdb.rating",
                          "cast_dir": {"$setIsSubset": ["$cast", "$directors"]},
                          "cast": "$cast",
                          "directors": "$directors"}
             },
            {"$match": {"cast_dir": True}
             },
            {"$project": {"title": "$title",
                          "rating": "$rating"}}])
        print_results(result)


def zad_3():
    with get_connection() as client:
        result = client['db-aggregations']['movies'].aggregate(
            [
                {'$unwind': {'path': '$cast'}},
                {'$group': {'_id': '$cast', 'aver': {'$avg': '$imdb.rating'}}},
                {'$sort': {'aver': -1}},
                {'$limit': 10}
            ])
        print_results(result, 10)


def zad_4():
    with get_connection() as client:
        result = client['db-aggregations']['air_alliances'].aggregate([
            {'$unwind': {'path': '$airlines'}},
            {'$lookup': {'from': 'air_routes', 'localField': 'airlines', 'foreignField': 'airline.name', 'as': 'routes'}},
            {'$unwind': {'path': '$routes'}},
            {'$match': {'routes.dst_airport': 'BCN'}},
            {'$group': {'_id': '$name', 'routes_cnt': {'$sum': 1}}},
            {'$sort': {'routes_cnt': -1}}, 
            {'$limit': 1}
        ])
        print_results(result, 1)


def zad_5():
    with get_connection() as client:
        result = client['db-aggregations']['air_routes'].aggregate([
            {'$graphLookup': {
                'from': 'air_routes',
                'startWith': "$dst_airport",
                'connectFromField': "dst_airport",
                'connectToField': 'src_airport',
                'maxDepth': 1,
                'as': "destinations",
                'depthField': "stops_after"
            }},
            {'$match': {'src_airport': "BNC"}},
            {'$project': {'src_airport': '$src_airport', 'dst_airport': '$dst_airport', 'destinations': '$destinations'}},
            {'$unwind': {'path': '$destinations'}},
            {'$group': {
                '_id': {"src": '$src_airport'},
                "dst_max_2": {"$addToSet": "$destinations.dst_airport"}}}

        ])
        print_results(result, 2)


def zad_9():
    with get_connection() as client:
        result = client["db-aggregations"]["movies"].aggregate([
            {'$match': {'imdb.rating': {'$gt': 0},'runtime': {'$gt': 100}}},
            {'$facet': {
                    'topFive': [{'$sort': {'imdb.rating': -1}}, {'$limit': 5}],
                    'topFiveRuns': [{'$sort': {'runtime': -1}}, {'$limit': 5}]}
            }
        ])
        print_results(result, 5)

zad_9()