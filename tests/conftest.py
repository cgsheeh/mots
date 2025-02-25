# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Test configuration and fixtures."""


import pytest
from mots.config import FileConfig


@pytest.fixture
def repo(tmp_path, config):
    """Create a file structure in the file system and initialize a repo config.

    The below directory and file structure was created to provide different
    opportunities for categorizing the paths within each directory. This was done in
    the hope that it will make it easier to understand the different module definitions
    in other fixtures and tests.
    """
    test_repo = tmp_path / "test_repo"
    test_repo.mkdir()

    [
        (test_repo / ".hg").mkdir(),
        (test_repo / "canines").mkdir(),
        (test_repo / "canines" / "chihuahuas").mkdir(),
        (test_repo / "canines" / "chihuahuas" / "apple_head").touch(),
        (test_repo / "canines" / "beagle").touch(),
        (test_repo / "canines" / "corgy").touch(),
        (test_repo / "canines" / "red_fox").touch(),
        (test_repo / "canines" / "hyena").touch(),
        (test_repo / "felines").mkdir(),
        (test_repo / "felines" / "persian").touch(),
        (test_repo / "felines" / "cheetah").touch(),
        (test_repo / "bovines").mkdir(),
        (test_repo / "bovines" / "cow").touch(),
        (test_repo / "bovines" / "sheep").touch(),
        (test_repo / "pigs").mkdir(),
        (test_repo / "pigs" / "wild_boar").touch(),
        (test_repo / "pigs" / "miniature_pig").touch(),
        (test_repo / "marsupials").mkdir(),
        (test_repo / "marsupials" / "kangaroo").touch(),
        (test_repo / "marsupials" / "koala").touch(),
        (test_repo / "birds").mkdir(),
        (test_repo / "birds" / "parrot").touch(),
        (test_repo / "birds" / "eagle").touch(),
    ]

    file_config = FileConfig(test_repo / "mots.yml")
    file_config.config = config
    file_config.write()

    return test_repo


@pytest.fixture
def config():
    people = [
        {"info": "testing", "name": "jane", "nick": "jane", "bmo_id": 0},
        {"info": "testing", "name": "jill", "nick": "jill", "bmo_id": 1},
        {"info": "testing", "name": "otis", "nick": "otis", "bmo_id": 2},
    ]
    return {
        "repo": "test_repo",
        "created_at": "2021-09-10 12:53:22.383393",
        "updated_at": "2021-09-10 12:53:22.383393",
        "people": people,
        "modules": [
            {
                "machine_name": "domesticated_animals",
                "exclude_submodule_paths": True,
                "exclude_module_paths": True,
                "includes": [
                    "canines/**/*",
                    "felines/**/*",
                    "bovines/**/*",
                    "birds/**/*",
                    "pigs/**/*",
                ],
                "excludes": ["canines/red_fox"],
                "owners": [people[0]],
                "peers": [people[1]],
                "submodules": [
                    {
                        "machine_name": "predators",
                        "includes": [
                            "canines/hyena",
                            "felines/tiger",
                            "felines/cheetah",
                            "birds/**/*",
                        ],
                        "excludes": [
                            "birds/parrot",
                        ],
                        "owners": [people[1]],
                    }
                ],
            },
            {
                "machine_name": "pets",
                "includes": [
                    "canines/**/*",
                    "felines/**/*",
                    "birds/**/*",
                ],
                "excludes": [
                    "canines/red_fox",
                    "canines/hyena",
                    "felines/cheetah",
                    "birds/eagle",
                ],
                "owners": [people[2]],
                "peers": [people[1]],
            },
        ],
    }
