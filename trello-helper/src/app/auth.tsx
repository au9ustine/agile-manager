import * as React from 'react';
import { Theme, createStyles, makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import { TextField, Button } from '@material-ui/core';
import Grid from "@material-ui/core/Grid";

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    root: {
      padding: theme.spacing(3, 2),
      margin: theme.spacing(3),
    },
    textfield: {
      marginTop: theme.spacing(1),
      marginLeft: theme.spacing(2),
      width: 640,
    },
    form: {
      display: 'flex',
      flexDirection: 'column'
    },
    button: {
      margin: theme.spacing(2),
      width: 200
    }
  }),
);

export default function Authentication() {
  const classes = useStyles();
  return (
    <Paper className={classes.root}>
      <Typography variant="h5" component="h3">
        请填入 API Key 和 Server Token
      </Typography>
      <form autoComplete="off" className={classes.form}>
        <TextField
          required
          className={classes.textfield}
          label="API Key"
          margin="normal" />
        <TextField
          className={classes.textfield}
          label="Server Token"
          margin="normal" />
        <Button
          className={classes.button}
          variant="contained"
          color="primary"
          size="large"
        >Authenticate</Button>
      </form>
    </Paper>
  )
}
