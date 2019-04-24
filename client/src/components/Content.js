import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import { fade } from '@material-ui/core/styles/colorManipulator';
import Grid from '@material-ui/core/Grid';
import SearchIcon from '@material-ui/icons/Search';
import InputBase from '@material-ui/core/InputBase';
import Button from '@material-ui/core/Button';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Switch from '@material-ui/core/Switch';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import MenuItem from '@material-ui/core/MenuItem';
import CircularProgress from '@material-ui/core/CircularProgress';

const axios = require('axios');

const BootstrapInput = withStyles(theme => ({
    root: {
        'label + &': {
            marginTop: theme.spacing.unit * 3,
        },
    },
    input: {
        borderRadius: 4,
        position: 'relative',
        backgroundColor: 'white',
        border: '1px solid #ced4da',
        fontSize: 16,
        width: 'auto',
        padding: '10px 26px 10px 12px',
        transition: theme.transitions.create(['border-color', 'box-shadow']),
        '&:focus': {
            borderRadius: 4,
            borderColor: '#80bdff',
            boxShadow: '0 0 0 0.2rem rgba(0,123,255,.25)',
        },
    },
}))(InputBase);

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
        paddingTop: 5,
        paddingRight: theme.spacing.unit,
        paddingBottom: 0,
        fontSize: "larger",
        paddingLeft: theme.spacing.unit * 10,
        transition: theme.transitions.create('width'),
        height: 44,
        width: '100%',
    },
    Headercard: {
        width: "-webkit-fill-available",
        marginBottom: 15,
        background: "#322f53",
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
    },
    FormControlLabel: {
        // marginLeft: 10,
    },
    bootstrapFormLabel: {
        fontSize: 18,
        color: "white",
        marginTop: "0.5em",
        marginLeft: "1em",
        marginRight: "1em",
        // display: "contents",
    },
    margin: {
        display: "-webkit-box",
        marginBottom: "1em",
    },
});


class Content extends Component {
    constructor() {
        super();

        this.state = {
            searchword : "",
            labels : null,
            clusterData: null,
            currentLabel: null,
            checkedA: false,
            cluster: 0,
        }

        this.getdata = this.getdata.bind(this)
        this.handleClickSearch = this.handleClickSearch.bind(this)
        this.handleClickLabel = this.handleClickLabel.bind(this)
        this.handleSelect = this.handleSelect.bind(this)
        this.handleChange = this.handleChange.bind(this)
    }

    handleSelect = name => event => {
        this.setState({ [name]: event.target.value });
    };

    handleChange = name => event => {
        this.setState({ [name]: event.target.checked });
        // this.handleClickSearch();
    };

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
        var pathfile = "tfidf/" + word + '.json'
        pathfile = this.state.checkedA ? pathfile : "no" + pathfile
        
        // const webpath = '/datas/' + pathfile 
        const webpath = 'https://public.siwanont.ml/KmLx7EM2GuwEeDQejBufJfgP+nXga5j8/' + pathfile
        // const webpath = 'http://localhost:5000/api/cluster/' + word

        const response = await axios.get(webpath, {})
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
        const { clusterData, labels, currentLabel, searchword, checkedA, cluster } = this.state
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
                        <Card className={classes.Headercard} style={{ padding: "1em" }}> 
                            <CardContent style={{ padding: "0em" }}>
                                <FormControl style={{ display: "-webkit-box", }}>
                                    <Typography className={classes.bootstrapFormLabel}>Min Cluster</Typography>
                                    <Select
                                        value={this.state.cluster}
                                        onChange={this.handleSelect('cluster')}
                                        input={<BootstrapInput name="cluster"/>}
                                    >
                                        {Array.from(Array(10).keys()).map((item) => (
                                            <MenuItem key={item} value={5*item}>{5*item}</MenuItem>
                                        ))
                                        }
                                    </Select>
                                    <Typography className={classes.bootstrapFormLabel}>TF-IDF</Typography>
                                    <FormControlLabel className={classes.FormControlLabel}
                                        control={
                                            <Switch
                                                checked={checkedA}
                                                onChange={this.handleChange('checkedA')}
                                                value="checkedA"
                                                color="primary"
                                            />
                                        }
                                    />
                                </FormControl>
                            </CardContent>
                        </Card>
                        {labels !== null ?
                            <Card className={classes.card}>
                                <CardContent className={classes.cardcontent}>
                                    {labels.map(label => (
                                        label[1][0] > cluster ?
                                        <a href="/#" key={label[0]} value={label[0]} onClick={this.handleClickLabel} style={{display: 'block', color: 'white', fontSize: "medium",}}>
                                            {label[0]} {"(" + (label[1][1] * 100).toFixed(2) + "% , " + label[1][0] + ")"}
                                        </a>
                                        : null
                                    ))}
                                </CardContent>
                            </Card>
                            : <CircularProgress
                                className={classes.progress}
                                variant="determinate"
                                value={this.state.completed}
                            />
                        }
                    </Grid>
                    <Grid item xs={12} sm={9} >
                        <Card className={classes.Headercard} style={{ background: "none repeat scroll 0 0 #1F1D33", minHeight: "80px",}}>
                            <CardContent>
                                {currentLabel !== null ? 
                                    <Typography variant="h4" component="h3" style={{ color: "white"}}>
                                        {currentLabel} 
                                    </Typography>
                                    : <Typography variant="h4" component="h3" style={{ color: "white" }}>
                                        Input a word and Choose a label from the left-sided
                                    </Typography>
                                }
                            </CardContent>
                        </Card>
                        {currentLabel !== null && clusterData[currentLabel] !== null ? clusterData[currentLabel].map((item, index) => (
                            <Card key={`${currentLabel}-${index}`} className={classes.card}>
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