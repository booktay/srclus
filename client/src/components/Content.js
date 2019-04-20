import React, { Component } from 'react';
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

const axios = require('axios');
const fs = require("fs");

const styles = theme => ({
    rootGrid: {
        padding: "2%",
        paddingLeft: "3%",
    },
    button: {
        backgroundColor: "#476f2c",
        color: "white",
        fontSize: "larger",
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


class Content extends Component {
    constructor() {
        super();

        this.state = {
            searchword : "",
            labels : null,
            clusterData: null,
            currentLabel: null
        }

        this.getdata = this.getdata.bind(this)
        this.handleClickSearch = this.handleClickSearch.bind(this)
        this.handleClickLabel = this.handleClickLabel.bind(this)
    }

    handleClickSearch() {
        const word = this.state.searchword
        if (word !== "")
            this.getdata(word)
    }

    handleClickLabel(e) {
        const label = e.target.getAttribute('value')
        this.setState(state => {
            state.currentLabel = label
            return state
        })
    }
    
    async getdata(word) {
        var webpath = '/datas/' + word + '.json'
        // console.log(webpath)
        // if (!fs.existsSync(webpath)) {
        //     webpath = 'http://localhost:5000/api/cluster/' + word
        // }
        const response = await axios.get(webpath)
        // console.log(response)
        if (response.status === 200) {
            this.setState(state => {
                state.labels = response.data.rank
                state.clusterData = response.data.datas
                return state
            })
        }
    }

    render() {
        const { clusterData, labels, currentLabel, searchword } = this.state
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
                                placeholder="Search Thread Clustering"
                                classes={{
                                    root: classes.inputRoot,
                                    input: classes.inputInput,
                                }}
                                value={searchword}
                                onChange={e => this.setState({ searchword: e.target.value })}
                            />
                        </div>
                    </Grid>
                    <Grid className={classes.searchGrid} item xs={12} sm={2}>
                        <Button className={classes.button} variant="contained" fullWidth size="large" onClick={this.handleClickSearch}>
                            Search
                        </Button>
                    </Grid>
                    <Grid item xs={12} sm={3}>
                        {labels !== null ?
                            <Card className={classes.card}>
                                <CardActionArea>
                                    <CardContent className={classes.cardcontent}>
                                        {labels.map(label => (
                                            label[1][0] > 1 ?
                                            <a href="/#" key={label[0]} value={label[0]} onClick={this.handleClickLabel} style={{display: 'block', color: 'white', fontSize: "medium",}}>
                                                    {label[0]} {"(" + (label[1][1] * 100).toFixed(2) + "% , " + label[1][0] + ")"}
                                            </a>
                                            : null
                                        ))}
                                    </CardContent>
                                </CardActionArea>
                            </Card>
                            : null
                        }
                    </Grid>
                    <Grid item xs={12} sm={9} >
                        {currentLabel !== null && clusterData[currentLabel] !== null ? clusterData[currentLabel].map((item, index) => (
                            <Card key={`${currentLabel}-${index}`} className={classes.card}>
                                <CardActionArea>
                                    <CardContent className={classes.cardcontent}>
                                        <Typography gutterBottom variant="h5" component="h2" className={classes.typetitle}>
                                            <a href={"https://pantip.com/topic/" + item.id} style={{ display: 'block', color: 'white', textDecoration: "none" }}>
                                                {item.title}
                                            </a>
                                    </Typography>
                                        <Divider variant="fullWidth" className={classes.divider} />
                                        <Typography component="p" className={classes.typedesc}>
                                            {item.desc.substr(0, 400) + " ..."}
                                </Typography>
                                    </CardContent>
                                </CardActionArea>
                            </Card>
                        ))
                            : null
                        }
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