#!/usr/bin/env python

import apt

def commit():
    return apt.Cache().commit(apt.progress.text.AcquireProgress(), \
                              apt.progress.text.OpProgress())

if __name__ == '__main__':
    commit()
