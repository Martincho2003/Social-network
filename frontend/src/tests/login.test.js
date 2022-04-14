import React from 'react';
import { render, screen } from '@testing-library/react';
import Login from '../components/Login';

test('render Sign In text', () => {
  render(<Login />);
  expect(screen.getByText('Sign In')).toBeInTheDocument();
});