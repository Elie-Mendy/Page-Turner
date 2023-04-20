import React, { useState } from 'react';
import { Form } from 'react-bootstrap';

function SearchBar({ onSearch }) {
  const [searchTerm, setSearchTerm] = useState('');

  const handleInputChange = (event) => {
    const value = event.target.value;
    setSearchTerm(value);
    onSearch(value);
  };

  return (
    <Form>
      <Form.Group>
        <Form.Control
          type="text"
          placeholder="Rechercher..."
          value={searchTerm}
          onChange={handleInputChange}
        />
      </Form.Group>
    </Form>
  );
}

export default SearchBar;