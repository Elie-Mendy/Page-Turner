import React, { useState, useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Row, Col } from 'react-bootstrap'
import Book from '../Components/Book'
import Loader from '../Components/Loader'
import Message from '../Components/Message'

import { listBooks } from '../actions/bookActions'

function HomeScreen() {

	const dispatch = useDispatch()
	const bookList = useSelector(state => state.bookList);
	const { loading, error, books } = bookList;

	useEffect(() => {
		dispatch(listBooks())
	}, [dispatch])
	return (
		<div>
			<h1>Latest Books</h1>
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
	)
}

export default HomeScreen