const SMOKES_PER_SCRAP = 5;
const METAL_FRAGMENTS_PER_SMOKE = 20;
const GUNPOWDER_PER_SMOKE = 18;


/**
 * User wants to get as much gunpowder as possible by recycling with scraps at vending machines.
 * @param numScrap : number
 * @return gunpowderObtained : number
 */
function ScrapToGPOnly(numScrap) {

    // If user does not get enough scrap to buy a single smoke
    if (numScrap < SMOKES_PER_SCRAP) {
        return 0;
    }
    let numSmokeGrenades;
    let metalFragments;
    let gunpowderObtained = 0;

    // While it is possible to buy smokes with the amount of scraps that we get
    while (numScrap >= SMOKES_PER_SCRAP) {
        numSmokeGrenades = Math.floor(numScrap / SMOKES_PER_SCRAP);
        metalFragments = numSmokeGrenades * METAL_FRAGMENTS_PER_SMOKE;
        gunpowderObtained += numSmokeGrenades * GUNPOWDER_PER_SMOKE;

        // Updating number of scraps by subtracting bought smokes and adding new scraps gained by selling metal frags
        numScrap = numScrap - numSmokeGrenades * SMOKES_PER_SCRAP + Math.floor(metalFragments / 25);
    }

    return gunpowderObtained;
}

/**
 * User can ask to keep a certain amount of metal frags that he wants to keep instead of recycling it all in gunpowder
 * @param numScrap : number
 * @param metalWanted : number or null (optional arg)
 * @return gunpowderObtained
 */


function NotScrapToGPOnly(numScrap, metalWanted = 0) {


    // If user does not get enough scrap to buy a single smoke
    if (numScrap < SMOKES_PER_SCRAP) {
        return 0;
    }

    // Case where user asks too much metal frags for what is it actually possible to get
    if (Math.floor(numScrap / 8) * 20 < metalWanted) {
        throw new Error("You can't get that much metal frags with" + (numScrap < 2 ? " this " : " these ") + (numScrap < 2 ? "scrap" : "scraps"));
    }

    // Calculate how many smoke grenades can be bought with the scraps
    let numSmokeGrenades = Math.floor(numScrap / SMOKES_PER_SCRAP);
    numScrap = numScrap - numSmokeGrenades * SMOKES_PER_SCRAP
    let metalFragments = numSmokeGrenades * METAL_FRAGMENTS_PER_SMOKE;

    // Calculate how much metal can be obtained from the metal fragments (considering metalWanted)
    let remainingMetalFragments = metalFragments - metalWanted

    // Calculate how many scraps can be obtained from the remaining metal fragments
    let scrapsFromMetalFragments = Math.floor(remainingMetalFragments / 25);

    // Calculate the total gunpowder obtained from the remaining scraps
    let gunpowderObtained = ScrapToGPOnly(numScrap + scrapsFromMetalFragments) + numSmokeGrenades * GUNPOWDER_PER_SMOKE

    return gunpowderObtained;
}

console.log(ScrapToGPOnly(33486))
console.log(NotScrapToGPOnly(100, 40))