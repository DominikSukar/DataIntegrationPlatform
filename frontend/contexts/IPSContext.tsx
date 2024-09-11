import { useContext, createContext, useState, useEffect } from "react";

import { DOMAIN } from "@/constants/api";

import { IIPSContextType } from "@/types/contextTypes"
import { ItemCollection, PerkCollection, SpellCollection } from "@/types/matchTypes";

const IPSContext = createContext<IIPSContextType|undefined>(undefined);

export const useIPSContext = () => {
  const context = useContext(IPSContext);
  if (context === undefined) {
    throw new Error('useGameDetails must be used within a GameDetailsProvider');
  }
  return context;
};

export function IPSContextProvider({children}: {
    children: React.ReactNode;
}) {
    const [items, setItems] = useState<ItemCollection|null>(null);
    const [perks, setPerks] = useState<PerkCollection|null>(null);
    const [spells, setSpells] = useState<SpellCollection|null>(null);
  
    useEffect(() => {
        const fetchData = async () => {
          const [itemsResponse, perksResponse, spellsResponse] = await Promise.all([
            fetch(`${DOMAIN}/datadragon/items/`),
            fetch(`${DOMAIN}/datadragon/perks/`),
            fetch(`${DOMAIN}/datadragon/summoners/`)
          ]);
    
          const [itemsData, perksData, spellsData] = await Promise.all([
            itemsResponse.json(),
            perksResponse.json(),
            spellsResponse.json()
          ]);
    
          setItems(itemsData);
          setPerks(perksData);
          setSpells(spellsData);
        };
    
        fetchData();
      }, []);


    return (
        <IPSContext.Provider value={{items, perks, spells}}>
            {children}
        </IPSContext.Provider>
    )
}
