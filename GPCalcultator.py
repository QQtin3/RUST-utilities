def scrapToGPOnly(numScrap):
    SMOKES_PER_SCRAP = 5
    METAL_FRAGMENTS_PER_SMOKE = 20
    GUNPOWDER_PER_SMOKE = 18
    METAL_FRAGMENTS_PER_SCRAP = 25

    if numScrap < SMOKES_PER_SCRAP:
        return 0

    gunpowderObtained = 0
    remainingMetalFragments = 0

    while numScrap >= SMOKES_PER_SCRAP:
        numSmokeGrenades = numScrap // SMOKES_PER_SCRAP
        metalFragments = numSmokeGrenades * METAL_FRAGMENTS_PER_SMOKE
        gunpowderObtained += numSmokeGrenades * GUNPOWDER_PER_SMOKE
        numScrap = numScrap - numSmokeGrenades * SMOKES_PER_SCRAP + \
                   (metalFragments + remainingMetalFragments) // METAL_FRAGMENTS_PER_SCRAP

        remainingMetalFragments = (metalFragments + remainingMetalFragments) % METAL_FRAGMENTS_PER_SCRAP

    return gunpowderObtained


def notScrapToGPOnly(numScrap, metalWanted=0):
    SMOKES_PER_SCRAP = 5
    METAL_FRAGMENTS_PER_SMOKE = 20
    GUNPOWDER_PER_SMOKE = 18
    METAL_FRAGMENTS_PER_SCRAP = 25

    if numScrap < SMOKES_PER_SCRAP:
        return 0

    if numScrap // SMOKES_PER_SCRAP * METAL_FRAGMENTS_PER_SMOKE < metalWanted:
        return 0

    numSmokeGrenades = numScrap // SMOKES_PER_SCRAP
    numScrap -= numSmokeGrenades * SMOKES_PER_SCRAP
    metalFragments = numSmokeGrenades * METAL_FRAGMENTS_PER_SMOKE
    remainingMetalFragments = metalFragments - metalWanted
    scrapsFromMetalFragments = remainingMetalFragments // METAL_FRAGMENTS_PER_SCRAP

    gunpowderObtained = scrapToGPOnly(numScrap + scrapsFromMetalFragments) + numSmokeGrenades * GUNPOWDER_PER_SMOKE

    return gunpowderObtained


def main():
    try:
        print("Welcome! How many scraps do you want to recycle?")
        numScrap = int(input())

        print("Do you want to keep some metal fragments during the process? (Yes/No)")
        doKeepMetalFragments = input().lower() == "yes"

        print(f"You decided{' ' if doKeepMetalFragments else ' not '}to keep metal fragments during the process")

        if doKeepMetalFragments:
            print("How many metal frags do you want to keep?")
            numMetalFrags = int(input())
            print(
                f"With {numScrap} scraps you will get {notScrapToGPOnly(numScrap, numMetalFrags)} gunpowder and at least {numMetalFrags} metal fragments!")
        else:
            print(f"With {numScrap} scraps you will get {scrapToGPOnly(numScrap)} gunpowder!")
    except Exception as error:
        print(error)


main()
