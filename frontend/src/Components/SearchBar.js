import { useContext } from "react";
import { HomeScreenContext } from "../Context/HomeScreenContext";
import { Form, FormControl } from "react-bootstrap";

function SearchBar() {
    const {
        placeholder,
        searchValue,
        handleInputChange,
        handleSubmit,
    } = useContext(HomeScreenContext);


    return (
        <Form onSubmit={handleSubmit} className="row homepage-searchbar">
            <FormControl
                type="text"
                placeholder={placeholder}
                className="mr-sm-2 form-inline"
                value={searchValue}
                onChange={handleInputChange}
            />
        </Form>
    );
}

export default SearchBar;
