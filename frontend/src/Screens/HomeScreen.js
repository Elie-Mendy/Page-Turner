import React, { useState, useEffect, useContext } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Row, Col } from 'react-bootstrap'
import { HomeScreenContextProvider } from '../Context/HomeScreenContext'
import Book from '../Components/Book'
import Loader from '../Components/Loader'
import Message from '../Components/Message'
import HomepageDropdown from '../Components/HomepageDropdown'

import { listBooks } from '../actions/bookActions'




import SearchBar from '../Components/SearchBar';



function HomeScreen() {

  // flo recherche livre
  const [searchValue, setSearchValue] = useState("");

  const handleInputChange = (event) => {
    setSearchValue(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // Faites quelque chose avec la valeur de recherche
		// changer la requete dans BookAction
		dispatch(listBooks(searchValue))
  };

	const dispatch = useDispatch()
	const bookList = useSelector(state => state.bookList);
	const { loading, error, books } = bookList;

	useEffect(() => {
		dispatch(listBooks(searchValue))
	}, [dispatch, searchValue])

	return (
		<HomeScreenContextProvider>
			<div>
				<Row>
					<Col>
						<HomepageDropdown/>
					</Col>

					<Col>
						<SearchBar
							searchValue={searchValue}
							handleInputChange={handleInputChange}
							handleSubmit={handleSubmit}
						/>
					</Col>
				</Row>
				{ loading && <Loader/>}
				{ error && <Message variant='danger'>{error}</Message>}
				
				{ books && books.items && (
					<Row>
						{ books.items.map(book => ( 
							<Col key={book.id} sm={12} md={6} lg={3}>
								<Book book={book} />
							</Col>
						))} 
					</Row>
					)
				}
				
			</div>
		</HomeScreenContextProvider>
	)
}

export default HomeScreen