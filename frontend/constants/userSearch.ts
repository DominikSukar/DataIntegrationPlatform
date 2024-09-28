import { z } from "zod";

export const defaultRegions = [
  {
    full_name: "Europe Nordic and East",
    symbol: "EUNE",
    riot_symbol: "EUN1",
    hostname: "eun1.api.riotgames.com",
    active: true,
    id: 1,
  },
  {
    full_name: "North America",
    symbol: "NA",
    riot_symbol: "NA1",
    hostname: "na1.api.riotgames.com",
    active: true,
    id: 6,
  },
];

export const formSchema = z.object({
  username: z.string().min(2, {
    message: "Username must be at least 2 characters.",
  }),
});
