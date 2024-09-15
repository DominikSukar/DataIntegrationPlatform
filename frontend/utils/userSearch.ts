import Cookies from "js-cookie";

export const getSavedRegion = () => {
  const savedRegion = Cookies.get("selectedRegion");
  return savedRegion && regions.includes(savedRegion) ? savedRegion : regions[0];
};

export const getSavedSummoners = () => {
  const summonersCookie = Cookies.get("summonersSearch");
  return summonersCookie ? JSON.parse(summonersCookie) : [""];
};

export const updateSummonersSearch = (searchEntry: string, region: string) => {
  let summonersSearchCookie = Cookies.get("summonersSearch");
  let summonersSearch = summonersSearchCookie ? JSON.parse(summonersSearchCookie) : [];

  summonersSearch = summonersSearch.filter((entry: string) => entry !== searchEntry);
  summonersSearch.unshift(searchEntry);
  summonersSearch = summonersSearch.slice(0, 10);

  Cookies.set("summonersSearch", JSON.stringify(summonersSearch), { expires: 365 });
};

export const saveRegion = (region: string) => {
  Cookies.set("selectedRegion", region, { expires: 365 });
};