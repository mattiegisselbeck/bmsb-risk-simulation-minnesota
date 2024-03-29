from sqlalchemy import create_engine

__status__ = "Production"

class Database:
    def __init__(self, host: str, user: str, password: str, db_name: str, port: int) -> None:
        """Instantiates a database connection to a PostgreSQL database.

        :param str host: Host address of the database you would like to access.
        :param str user: Username credential for the database you would like to access.
        :param str password: Password credential for the database you would like to access.
        :param str db_name: Name of the database that you would like to access.
        :param int port: Port number of the database.
        """

        self.engine = create_engine(f'postgresql://postgres:H<8Y$Ya5RF\"QKz;@35.192.156.119:5432/sandbox', echo=False)

    def query(self, query: str, user_input: int) -> str:
        with self.engine.connect() as connection:
            try:
                result = connection.execute(query, (int(user_input),))
                return result.fetchall()
            except Exception as e:
                return "Error: " + str(e)

class Query:
    """
    A class used to store SQL queries.
    """

    # Huff Model Queries
    HUFFMODELIN = """
    SELECT json_build_object(
    'type', 'FeatureCollection',
    'features', json_agg(ST_AsGeoJSON(rankings.*)::json))
        FROM (
            SELECT *, RANK() OVER (ORDER BY Incoming DESC) as rank
            FROM huff_model
        ) as rankings
        WHERE rank <= %s;
    """
    HUFFMODELOUT = """
        SELECT json_build_object(
        'type', 'FeatureCollection',
        'features', json_agg(ST_AsGeoJSON(rankings.*)::json))
        FROM (
            SELECT *, RANK() OVER (ORDER BY Outgoing DESC) as rank
            FROM huff_model
        ) as rankings
        WHERE rank <= %s;
    """
    HUFFMODELRISK = """
        SELECT json_build_object(
        'type', 'FeatureCollection',
        'features', json_agg(ST_AsGeoJSON(rankings.*)::json))
        FROM (
            SELECT *, RANK() OVER (ORDER BY Risk DESC) as rank
            FROM huff_model
        ) as rankings
        WHERE rank <= %s;
    """

    # Huff Model with Distance Decay Queries
    HUFFMODELDDIN = """
        SELECT json_build_object(
        'type', 'FeatureCollection',
        'features', json_agg(ST_AsGeoJSON(rankings.*)::json))
        FROM (
            SELECT *, RANK() OVER (ORDER BY Incoming DESC) as rank
            FROM huff_model_distance_decay
        ) as rankings
        WHERE rank <= %s;
    """
    HUFFMODELDDOUT = """
        SELECT json_build_object(
        'type', 'FeatureCollection',
        'features', json_agg(ST_AsGeoJSON(rankings.*)::json))
        FROM (
            SELECT *, RANK() OVER (ORDER BY Outgoing DESC) as rank
            FROM huff_model_distance_decay
        ) as rankings
        WHERE rank <= %s;
    """
    HUFFMODELDDRISK = """
        SELECT json_build_object(
        'type', 'FeatureCollection',
        'features', json_agg(ST_AsGeoJSON(rankings.*)::json))
        FROM (
            SELECT *, RANK() OVER (ORDER BY Risk DESC) as rank
            FROM huff_model_distance_decay
        ) as rankings
        WHERE rank <= %s;
    """

    # Gravity Model Queries
    GRAVITYMODELIN = """
        SELECT json_build_object(
        'type', 'FeatureCollection',
        'features', json_agg(ST_AsGeoJSON(rankings.*)::json))
        FROM (
            SELECT *, RANK() OVER (ORDER BY incoming DESC) as rank
            FROM gravity_model
        ) as rankings
        WHERE rank <= %s;
    """
    GRAVITYMODELOUT = """
        SELECT json_build_object(
        'type', 'FeatureCollection',
        'features', json_agg(ST_AsGeoJSON(rankings.*)::json))
        FROM (
            SELECT *, RANK() OVER (ORDER BY Outgoing DESC) as rank
            FROM gravity_model
        ) as rankings
        WHERE rank <= %s;
    """
    GRAVITYMODELRISK = """
        SELECT json_build_object(
        'type', 'FeatureCollection',
        'features', json_agg(ST_AsGeoJSON(rankings.*)::json))
        FROM (
            SELECT *, RANK() OVER (ORDER BY Risk) as rank
            FROM gravity_model
        ) as rankings
        WHERE rank <= %s;
    """
