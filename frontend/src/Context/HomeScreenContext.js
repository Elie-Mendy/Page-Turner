import { createContext, useState } from "react";

export const HomeScreenContext = createContext();

export function HomeScreenContextProvider({children}) {
  const [searchType, setSearchType] = useState(1);
  const [placeholder, setPlaceholder] = useState("Livres les plus récents");

  const handleSearchType = (searchType) => {
    switch(searchType) {
      case "tab1":
        setPlaceholder("Livres les plus récents");
        break;
      case "tab2":
        setPlaceholder("Recherche par similarité");
        break;
      default:
        setPlaceholder("Recherche par gouts d'utilisateurs");
        break;
    }
    setSearchType(searchType);
  }


  const data = { searchType, placeholder, handleSearchType };

  return (
    <HomeScreenContext.Provider value={data}>
      {children}
    </HomeScreenContext.Provider>
  );
}