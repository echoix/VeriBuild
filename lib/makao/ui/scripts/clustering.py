# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is MAKAO.
#
# The Initial Developer of the Original Code is
# Bram Adams (bramATcsDOTqueensuDOTca).
# Portions created by the Initial Developer are Copyright (C) 2006-2010
# the Initial Developer. All Rights Reserved.
#
# Contributor(s):
#
# ***** END LICENSE BLOCK *****

def cluster_weak():
    clusts = weakComponentClusters()

    for z in clusts:
        z.color = randomColor(120)

def cluster_bi():
    clusts = biComponentClusters()

    for z in clusts:
        z.color = randomColor(120)

def cluster_between(arg):
    clusts = edgeBetweennessClusters(arg)

    for z in clusts:
        z.color = randomColor(120)

