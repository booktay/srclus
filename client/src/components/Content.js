import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import { fade } from '@material-ui/core/styles/colorManipulator';
import Grid from '@material-ui/core/Grid';
import SearchIcon from '@material-ui/icons/Search';
import InputBase from '@material-ui/core/InputBase';
import Button from '@material-ui/core/Button';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';

const styles = theme => ({
    root: {
        flexGrow: 1,
        padding: "2%",
    },
    grow: {
        flexGrow: 1,
    },
    contentH : {
        marginTop: "0.5%",
        display: "inline-flex",
    },
    search: {
        position: 'relative',
        borderRadius: theme.shape.borderRadius,
        backgroundColor: fade(theme.palette.common.white, 0.15),
        '&:hover': {
            backgroundColor: fade(theme.palette.common.white, 0.25),
        },
        // marginRight: theme.spacing.unit * 2,
        marginLeft: 0,
        width: '100%',
        // display: "inline",
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
        height: "6.5vh",
        width: '100%',
    },
    inputInput: {
        paddingTop: theme.spacing.unit,
        paddingRight: theme.spacing.unit,
        paddingBottom: theme.spacing.unit,
        paddingLeft: theme.spacing.unit * 10,
        transition: theme.transitions.create('width'),
        width: '100%',
    },
    button: {
        // margin: theme.spacing.unit,
        width: "25%",
        marginLeft: "20px",
        backgroundColor: "#476f2c",
        color: "white",
    },
    input: {
        display: 'none',
    },
    card: {
        width: "-webkit-fill-available",
        marginBottom: 15,
        background: "#322f53",
        // maxWidth: 345,
    },
    cardcontent: {
        minHeight: 100,
        color: "white",
        textAlign: "left",
    },
    typetitle: {
        color: "white",
    },
    typedesc : {
        color: "white", 
        fontSize: "medium",
        marginTop: 10,
    },
    divider : {
        backgroundColor: "white",
    }
});

function Content(props) {
    const { classes } = props;

    function handleClick(e) {
        e.preventDefault();
        console.log('The link was clicked.');
    }

    return (
        <div className={classes.root}>
            <Grid container spacing={24}>
                <Grid item xs={12} className={classes.contentH}>
                    <div className={classes.search}>
                        <div className={classes.searchIcon}>
                            <SearchIcon />
                        </div>
                        <InputBase
                            placeholder="Search Thread Clustering…"
                            fullWidth
                            classes={{
                                root: classes.inputRoot,
                                input: classes.inputInput,
                            }}
                            id="searchinp"
                        />
                    </div>
                    <Button variant="contained" id="searchbtn" fullWidth size="large" className={classes.button} onClick={handleClick}>
                        Search
                    </Button>
                </Grid>
                <Grid item xs={12} sm={3}>
                    <Card className={classes.card}>
                        <CardActionArea>
                            <CardContent className={classes.cardcontent}>
                                {/* <a href="" onClick={handleClick}>
                                    Click me 1
                                </a>
                                <a href="" onClick={handleClick}>
                                    Click me 2
                                </a> */}
                            </CardContent>
                        </CardActionArea>
                    </Card>
                </Grid>
                <Grid item xs={12} sm={9} >
                    <Card className={classes.card}>
                        <CardActionArea>
                            <CardContent className={classes.cardcontent}>
                                <Typography gutterBottom variant="h5" component="h2" className={classes.typetitle}>
                                    Lizard
                                </Typography>
                                <Divider variant="fullWidth" className={classes.divider} />
                                <Typography component="p" className={classes.typedesc}>
                                    Lizards are a widespread group of squamate reptiles, with over 6,000 species, ranging
                                    across all continents except Antarctica
                                </Typography>
                            </CardContent>
                        </CardActionArea>
                    </Card>
                </Grid>
            </Grid>
        </div>
    );
}

Content.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Content);