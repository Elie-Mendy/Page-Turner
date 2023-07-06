import { createContext, useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { listBooks } from "../Actions/bookActions";

export const HomeScreenContext = createContext();

export function HomeScreenContextProvider({ children }) {
    const [searchType, setSearchType] = useState(1);
    const [placeholder, setPlaceholder] = useState("Livres les plus récents");
    const [searchValue, setSearchValue] = useState("");

    const handleInputChange = (event) => {   
        setSearchValue(event.target.value);
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        dispatch(listBooks(searchValue, searchType));
    };

    const dispatch = useDispatch();
    const bookList = useSelector((state) => state.bookList);
    const { loading, error, books } = bookList;

    useEffect(() => {
        if (searchType === "tab1") {
            dispatch(listBooks(searchValue, searchType));
        }
    }, [dispatch, searchValue, searchType]);

    const handleSearchType = (searchType) => {
        switch (searchType) {
            case "tab1":
                setPlaceholder("Search for recent books");
                break;
            case "tab2":
                setPlaceholder("Search by similarity");
                break;
            default:
                setPlaceholder("Search by user taste");
                break;
        }
        setSearchType(searchType);
    };

    const context = {
        searchType,
        searchValue,
        setSearchValue,
        placeholder,
        handleSearchType,
        handleInputChange,
        handleSubmit,
        loading,
        error,
        books,
    };

    return (
        <HomeScreenContext.Provider value={context}>
            {children}
        </HomeScreenContext.Provider>
    );
}
