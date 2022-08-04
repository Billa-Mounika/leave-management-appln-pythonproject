from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from datetime import datetime
from flask import session
class appLogger:
    def __init__(self):
        cloud_config = {
            'secure_connect_bundle': 'secure-connect-leave-management.zip'
        }
        auth_provider = PlainTextAuthProvider(username='YdgtCOjJZOJCAgagoAcJgRQZ', password='jKl4CsDOlOanxIDRF_Q4ji+NPi4zfyI5F4+0aIB-_xFl.Az7qnDUZNMNoDFyZSqCg74q6qqX6rys5eZnSbiZIIwtEy848TN_ajEaghb6fPyUZZ_z5lPvOLd.EBTmkrbL')
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        self.session = cluster.connect()

    def log(self, tag, message):
        table_name= 'db_operation.log'
        timestamp=str(datetime.today().now())[:23]
        query=f"INSERT INTO {table_name} (id,email_id,timestamp, tag, message) VALUES (uuid(),'{session.get('email_id')}' ,'{timestamp}','{tag}', '{message}');"

        self.session.execute(query)

