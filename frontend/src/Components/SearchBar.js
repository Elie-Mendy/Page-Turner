import { useContext } from "react";
import { HomeScreenContext } from '../Context/HomeScreenContext'
import { Form, FormControl } from "react-bootstrap";

function SearchBar({searchValue, handleInputChange, handleSubmit}) {
  const { placeholder } = useContext(HomeScreenContext)
  return (
    <Form onSubmit={handleSubmit} className="row className= homepage-searchbar">
      <div>
        <FormControl
          type="text"
          placeholder={placeholder}
          className="mr-sm-2 "
          value={searchValue}
          onChange={handleInputChange}
        />
      </div>
    </Form>
  );
}

export default SearchBar;
