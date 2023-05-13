import { useContext } from "react";
import { HomeScreenContext } from "../Context/HomeScreenContext";
import { Form, FormControl } from "react-bootstrap";

function SearchBar({ handleInputChange, handleSubmit }) {
    const { placeholder, searchValue } = useContext(HomeScreenContext);
    return (
        <Form
            onSubmit={handleSubmit}
            className="row className= homepage-searchbar"
        >
            <FormControl
                type="text"
                placeholder={placeholder}
                className="mr-sm-2 "
                value={searchValue}
                onChange={handleInputChange}
            />
        </Form>
    );
}

export default SearchBar;
