namespace RUST_utilities
{
    class Program 
    {
        const int SMOKES_PER_SCRAP = 5;
        const int METAL_FRAGMENTS_PER_SMOKE = 20;
        const int GUNPOWDER_PER_SMOKE = 18;
        const int METAL_FRAGMENTS_PER_SCRAP = 25;


        /* Function used when user wants to get as much gunpowder as possible
         * by recycling with scraps at vending machines.
         */
        static int scrapToGPOnly(int numScrap) {
            // If user does not get enough scrap to buy a single smoke
            if (numScrap < SMOKES_PER_SCRAP) {
                return 0;
            }

            int gunpowderObtained = 0;
            int remainingMetalFragments = 0;

            // While it is possible to buy smokes with the amount of scraps that we get
            while (numScrap >= SMOKES_PER_SCRAP) {
                int numSmokeGrenades = numScrap / SMOKES_PER_SCRAP;
                int metalFragments = numSmokeGrenades * METAL_FRAGMENTS_PER_SMOKE;
                gunpowderObtained += numSmokeGrenades * GUNPOWDER_PER_SMOKE;
                // Updating number of scraps by subtracting bought smokes and adding new scraps gained by selling metal frags
                numScrap = numScrap - numSmokeGrenades * SMOKES_PER_SCRAP +
                           (metalFragments + remainingMetalFragments) / METAL_FRAGMENTS_PER_SCRAP;

                remainingMetalFragments = (metalFragments + remainingMetalFragments) % METAL_FRAGMENTS_PER_SCRAP;
            }

            return gunpowderObtained;
        }


        /* Function used when user wants to keep a certain amount of metal frags
         * instead of recycling it all in gunpowder
         */
        static int notScrapToGPOnly(int numScrap, int metalWanted = 0) {
            // If user does not get enough scrap to buy a single smoke
            if (numScrap < SMOKES_PER_SCRAP) {
                return 0;
            }

            // Case where user asks too much metal frags for what is it actually possible to get
            if (numScrap / SMOKES_PER_SCRAP * METAL_FRAGMENTS_PER_SMOKE < metalWanted) {
                return 0;
            }

            // Calculate how many smoke grenades can be bought with the scraps
            int numSmokeGrenades = numScrap / SMOKES_PER_SCRAP;
            numScrap -= numSmokeGrenades * SMOKES_PER_SCRAP;
            int metalFragments = numSmokeGrenades * METAL_FRAGMENTS_PER_SMOKE;

            // Calculate how much metal can be obtained from the metal fragments (considering metalWanted)
            int remainingMetalFragments = metalFragments - metalWanted;

            // Calculate how many scraps can be obtained from the remaining metal fragments
            int scrapsFromMetalFragments = remainingMetalFragments / METAL_FRAGMENTS_PER_SCRAP;

            // Calculate the total gunpowder obtained from the remaining scraps
            int gunpowderObtained = scrapToGPOnly(numScrap + scrapsFromMetalFragments) +
                                    numSmokeGrenades * GUNPOWDER_PER_SMOKE;

            return gunpowderObtained;
        }

        
        /*
         * First executed part of the program when started.
         */
        static void Main() {
            try
            {
                Console.WriteLine("Welcome! How many scraps do you want to recycle?");
                int numScrap = Convert.ToInt32(Console.ReadLine());

                Console.WriteLine("Do you want to keep some metal fragments during the process? (Yes/No)");
                bool doKeepMetalFragments = Console.ReadLine().ToLower() == "yes" ? true : false;

                Console.WriteLine("You decided" + (doKeepMetalFragments ? " " : " not ") +
                                  "to keep metal fragments during the process");

                if (doKeepMetalFragments)
                {
                    Console.WriteLine("How many metal frags do you want to keep?");
                    int numMetalFrags = Convert.ToInt32(Console.ReadLine());
                    Console.WriteLine("With " + numScrap + " scraps you will get " +
                                      notScrapToGPOnly(numScrap, numMetalFrags) +
                                      "gunpowder and at least " + numMetalFrags + " metal fragments!");
                }
                else
                {
                    Console.WriteLine("With " + numScrap + " scraps you will get " + scrapToGPOnly(numScrap) +
                                      " gunpowder!");
                }
            }
            catch (Exception error) {
                Console.WriteLine(error);
            }
        }
    }
}