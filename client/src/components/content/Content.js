import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import { fade } from '@material-ui/core/styles/colorManipulator';
import Grid from '@material-ui/core/Grid';
import SearchIcon from '@material-ui/icons/Search';
import InputBase from '@material-ui/core/InputBase';
import Button from '@material-ui/core/Button';
// import Card from '@material-ui/core/Card';
// import CardActionArea from '@material-ui/core/CardActionArea';
// import CardContent from '@material-ui/core/CardContent';
// import Typography from '@material-ui/core/Typography';
// import Divider from '@material-ui/core/Divider';

// const axios = require('axios');

const styles = theme => ({
    rootGrid: {
        padding: "2%",
        paddingLeft: "3%",
    },
    button: {
        backgroundColor: "#476f2c",
        color: "white",
    },
    searchGrid: {
        // padding: "5px",
    },
    search: {
        position: 'relative',
        borderRadius: theme.shape.borderRadius,
        backgroundColor: fade(theme.palette.common.white, 0.15),
        '&:hover': {
            backgroundColor: fade(theme.palette.common.white, 0.25),
        },
        marginRight: theme.spacing.unit * 2,
        marginLeft: 0,
        width: '100%',
        height: '100%',
    },
    searchIcon: {
        width: theme.spacing.unit * 9,
        height: '100%',
        position: 'absolute',
        pointerEvents: 'none',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        color: 'white',
    },
    inputRoot: {
        color: 'white',
        width: '100%',
    },
    inputInput: {
        paddingTop: theme.spacing.unit * 1.5,
        paddingRight: theme.spacing.unit,
        paddingBottom: theme.spacing.unit,
        paddingLeft: theme.spacing.unit * 10,
        transition: theme.transitions.create('width'),
        width: '100%',
    },
});


class Content extends Component {

    handleClick(e) {
        e.preventDefault();
        console.log('The link was clicked.');
    }
    
    render() {
        const { classes } = this.props;
        return (
            <React.Fragment >
                <Grid container spacing={24} className={classes.rootGrid}>
                    <Grid className={classes.searchGrid} item xs={12} sm={10}>
                        <div className={classes.search}>
                            <div className={classes.searchIcon}>
                                <SearchIcon />
                            </div>
                            <InputBase
                                id = "wordinp"
                                placeholder="Search Thread Clustering"
                                classes={{
                                    root: classes.inputRoot,
                                    input: classes.inputInput,
                                }}
                            />
                        </div>
                    </Grid>
                    <Grid className={classes.searchGrid} item xs={12} sm={2}>
                        <Button className={classes.button} variant="contained" id="searchbtn" fullWidth size="large" onClick={this.handleClick}>
                            Search
                        </Button>
                    </Grid>
                </Grid>
            </React.Fragment>
        );
    }
}

Content.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Content);