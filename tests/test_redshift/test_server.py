from __future__ import unicode_literals

import json
import sure  # noqa

import moto.server as server
from moto import mock_redshift

'''
Test the different server responses
'''


@mock_redshift
def test_describe_clusters():
    backend = server.create_backend_app("redshift")
    test_client = backend.test_client()

    res = test_client.get('/?Action=DescribeClusters')

    json_data = json.loads(res.data.decode("utf-8"))
    clusters = json_data['DescribeClustersResponse']['DescribeClustersResult']['Clusters']
    list(clusters).should.equal([])
