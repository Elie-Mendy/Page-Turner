import { useContext } from "react";
import { HomeScreenContext } from "../Context/HomeScreenContext";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSearch } from '@fortawesome/free-solid-svg-icons';
import { Button } from "react-bootstrap";

function SearchButton() {
    const { handleSubmit } = useContext(HomeScreenContext);

    return (
        <Button onClick={handleSubmit} variant="primary" className="btn btn-light" type="submit">
            <FontAwesomeIcon icon={faSearch} />
        </Button>
    );
}

export default SearchButton;
