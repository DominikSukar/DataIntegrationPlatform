import { ItemCollection, PerkCollection, SpellCollection } from "./matchTypes";

export interface IIPSContextType {
    items: ItemCollection|null;
    perks: PerkCollection|null;
    spells: SpellCollection|null;
  }