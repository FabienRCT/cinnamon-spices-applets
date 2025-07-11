#!/usr/bin/python3
### Made from /usr/bin/cinnamon-spice-updater

import os
import sys
import argparse
import json

class UpdateSpicesCache:
    def __init__(self):
        # ~ parser = argparse.ArgumentParser(description='Cinnamon Spice Cache Updater',
                                         # ~ epilog="spice-type should be 'applet', 'desklet', 'extension' or 'theme'.")
        # ~ parser.add_argument("--update-all", dest="update_all_caches", action="store_const", const=True,
                            # ~ help="Update all spice caches to their latest versions.")

        # ~ choices = ["applet", "desklet", "extension", "theme", "actions"]

        # ~ ex_group = parser.add_mutually_exclusive_group()
        # ~ ex_group.add_argument("--update", dest="update_spice_cache_of_type", action="store", choices=choices, metavar="<spice-type>",
                            # ~ help="Update spices cache of a given type")
        # ~ ex_group.add_argument("--list-simple", dest="list_simple_spice_type", action="store", choices=choices, metavar="<spice-type>",
                            # ~ help="Simple list of UUIDs (or theme names) with available updates, for a given type")
        # ~ ex_group.add_argument("--list-json", dest="list_json_spice_type", action="store", choices=choices, metavar="<spice-type>",
                            # ~ help="Prints complete information on updates for spices of a given type, formatted as json.")
        # ~ args = parser.parse_args()

        # ~ if len(sys.argv) == 1:
            # ~ parser.print_help()
            # ~ exit(1)

        try:
            import cinnamon
            self.updater = cinnamon.UpdateManager()
            self.update_all_caches()
            # ~ if args.update_all_caches:
                # ~ self.update_all_caches()
            # ~ else:
                # ~ self.update_spice_cache_of_type(args.update_spice_cache_of_type)
                # ~ #self.list_simple(args.list_simple_spice_type)
                # ~ #self.list_json(args.list_json_spice_type)
        except Exception as e:
            print("Cinnamon updates failed: %s" % e)

    def update_all_caches(self):
        self.updater.refresh_all_caches()

    def update_spice_cache_of_type(self, spice_type):
        if spice_type is None:
            return

        self.updater.refresh_cache_for_type(spice_type)

    def list_simple(self, spice_type):
        if spice_type is None:
            return

        self.updater.refresh_cache_for_type(spice_type)
        updates = self.updater.get_updates_of_type(spice_type)

        for update in updates:
            print(update.uuid)

    def list_json(self, spice_type):
        if spice_type is None:
            return

        self.updater.refresh_cache_for_type(spice_type)
        updates = self.updater.get_updates_of_type(spice_type)

        jsonified_updates = {}

        for update in updates:
            jsonified_updates[update.uuid] = update.__dict__

        print(json.dumps(jsonified_updates, sort_keys=True, indent=4))

if __name__ == "__main__":
    if os.getuid() == 0:
        print("Error: Do not run this as root")
        exit(1)

    UpdateSpicesCache()

    exit(0)
