import React, { Component, Fragment } from 'react'

export default class Maincontent extends Component {
    render() {
        return (
            <Fragment>
                id = {this.props.id}
                <br/>
                {this.props.body}
                <br/>
                <hr/>
            </Fragment>
        )
    }
}

function addCard() {
    return (
        <React.Fragment>
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
        </React.Fragment>
    );
}

function getdata() {
    axios.get('/datas/apple.json')
        .then(function (response) {
            // handle success
            console.log(response);
        });
}

const styles = theme => ({
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
    typedesc: {
        color: "white",
        fontSize: "medium",
        marginTop: 10,
    },
    divider: {
        backgroundColor: "white",
    }
});
