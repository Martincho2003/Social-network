import React from 'react';
import { useHistory } from 'react-router-dom';

const SuccessSignUp = () => {
    const history = useHistory();

    const handleClick = () => {
        history.push("/login");
    }

    return (
        <div className="auth-wrapper form_body">
				<div className="auth-inner">

						<h3>Successfully signed in!</h3>
						<button type="submit" className="btn btn-primary btn-block" onClick={handleClick}>Log in</button>
						
				</div>
			</div>
    );
}

export default SuccessSignUp;