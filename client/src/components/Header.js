import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';

const styles = {
    root: {
        flexGrow: 1,
    },
    grow: {
        flexGrow: 1,
    },
    navbar: {
        background: "#38355c",
        // padding: "2%",
    },
    logo: {
        maxWidth: "5%",
        // marginLeft: "0%",
    },
    headername: {
        marginLeft: "1%",
        marginTop: "0%",
    },
    authorname: {
        marginRight: "1%",
        marginTop: "0%",
    },
};

function Header(props) {
    const { classes } = props;

    return (
        <div className={classes.root}>
            <AppBar position="static" className={classes.navbar}>
                <Toolbar>
                    <img src={process.env.PUBLIC_URL + '/images/pantip.png'} className={classes.logo} alt="logo" /> 
                    <Typography variant="h5" color="inherit" className={classes.headername}>
                        Search Result Clustering on Thai Internet Forum
                    </Typography>
                    <div className={classes.grow} />
                    <Typography variant="h6" color="inherit" className={classes.authorname}>
                        Siwanont Sittinam
                    </Typography>
                    <img src={process.env.PUBLIC_URL + '/images/mike.png'} className={classes.logo} alt="logo" /> 
                </Toolbar>
            </AppBar>
        </div>
    );
}

Header.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Header);