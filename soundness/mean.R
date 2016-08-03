teamA = read.table("PAN2016.OUTPUT.HHU.Overlap.pairsA.txt", header=FALSE)
lapply(teamA[1], mean)

teamB = read.table("PAN2016.OUTPUT.HHU.Overlap.pairsB.txt", header=FALSE)
lapply(teamB[1], mean)

teamC = read.table("PAN2016.OUTPUT.HHU.Overlap.pairsC.txt", header=FALSE)
lapply(teamC[1], mean)