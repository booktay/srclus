import React, { Component } from 'react'
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';

const styles = theme => ({
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
    typedesc: {
        color: "white",
        fontSize: "medium",
        marginTop: 10,
    },
    divider: {
        backgroundColor: "white",
    }
});

class Cardthread extends Component {

    render() {
        const { classes } = this.props;

        return (
            <React.Fragment>
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
            </React.Fragment>
        )
    }
}

Cardthread.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Cardthread);