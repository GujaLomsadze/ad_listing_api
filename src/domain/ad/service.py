from .queries import GET_ALL_ADS_WITH_OFFSET


def get_ads(db, start_from, limit):
    with db.cursor() as curs:
        curs.execute(GET_ALL_ADS_WITH_OFFSET)

        data = curs.fetchall()

        return data
