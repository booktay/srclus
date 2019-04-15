import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';

const styles = theme => ({
    root: {
        flexGrow: 1,
        // padding: "2%",
    },
    contentH: {
        marginTop: "0.5%",
        display: "inline-flex",
    },
    button: {
        // margin: theme.spacing.unit,
        width: "25%",
        marginLeft: "20px",
        backgroundColor: "#476f2c",
        color: "white",
    },
    input: {
        // display: 'none',
    },
    card: {
        // minWidth: 275,
    },
    title: {
        // fontSize: 14,
    },
    pos: {
        // marginBottom: 12,
    },
});

function Maincontent(props) {
    const { classes } = props;

    return (
        <div className={classes.root}>
            <Grid item xs={12} sm={3} className={classes.contentH}>
                <Paper className={classes.paper}>xs=12 sm=6</Paper>
            </Grid>
            <Grid item xs={12} sm={9} className={classes.contentH}>
                <Paper className={classes.paper}>xs=12 sm=6</Paper>
            </Grid>
            {/* <div className={classes.contentH}>
                <Card className={classes.card}>
                    <CardContent>
                        <Typography className={classes.title} color="textSecondary" gutterBottom>
                            Word of the Day
                        </Typography>
                        <Typography variant="h5" component="h2">
                            llll
                        </Typography>
                        <Typography className={classes.pos} color="textSecondary">
                            adjective
                        </Typography>
                        <Typography component="p">
                            well meaning and kindly.
                        <br />
                            {'"a benevolent smile"'}
                        </Typography>
                    </CardContent>
                    <CardActions>
                        <Button size="small">Learn More</Button>
                    </CardActions>
                </Card>
            </div>
            <div className={classes.contentH}>
                <Card className={classes.card}>
                    <CardContent>
                        <Typography className={classes.title} color="textSecondary" gutterBottom>
                        Word of the Day
                        </Typography>
                    </CardContent>
                </Card>
            </div> */}
        </div>
    );
}

Maincontent.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Maincontent);