import React from "react";
import { Form, FormControl, Button } from "react-bootstrap";

function FloSearchBar(props) {
  return (
    <Form inline onSubmit={props.handleSubmit}>
      <FormControl
        type="text"
        placeholder="Rechercher..."
        className="mr-sm-2"
        value={props.searchValue}
        onChange={props.handleInputChange}
      />
      <Button type="submit" variant="outline-success">
        Go
      </Button>
    </Form>
  );
}

export default FloSearchBar;
