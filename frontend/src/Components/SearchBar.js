import React from "react";
import { Form, FormControl } from "react-bootstrap";

function SearchBar(props) {
  return (
    <Form onSubmit={props.handleSubmit} className="row className= homepage-searchbar">
      <div>
        <FormControl
          type="text"
          placeholder="Rechercher..."
          className="mr-sm-2 "
          value={props.searchValue}
          onChange={props.handleInputChange}
        />
      </div>
    </Form>
  );
}

export default SearchBar;
