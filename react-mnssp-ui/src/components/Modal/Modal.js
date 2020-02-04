import React from 'react'
import { makeStyles } from '@material-ui/core/styles'
import Modal from '@material-ui/core/Modal'
import { Button } from '@material-ui/core'
import './modal.css'

function getModalStyle() {
    const top = 50 + 6
    const left = 50 + 6
  
    return {
      top: `${top}%`,
      left: `${left}%`,
      transform: `translate(-${top}%, -${left}%)`
    }
  }
  
  const useStyles = makeStyles(theme => ({
    paper: {
      position: 'absolute',
      width: 1300,
      minHeight: 700,
      maxHeight: 700,
      backgroundColor: theme.palette.background.paper,
      border: '2px solid #000',
      boxShadow: theme.shadows[5],
      padding: theme.spacing(2, 4, 3),
      overflowY: 'scroll'
    }
  }))
  
  const ModalInfo = ({
    name,
    data
  }) => {
    const classes = useStyles()
    const [modalStyle] = React.useState(getModalStyle)
    const [open, setOpen] = React.useState(false)
  
    const handleOpen = () => {
      setOpen(true)
    }
  
    const handleClose = () => {
      setOpen(false)
    }
  
    const title = name ? name.slice(0, 37) : name
  
    return (
      <div>
        {event && <div onClick={handleOpen}>{title}</div>}
  
        {course && <div onClick={handleOpen}>{title}</div>}
  
        {infoModal && (
          <ul className='modal-title' onClick={handleOpen}>
            <Button className={'Button'} onClick={handleOpen}>
              More Info
            </Button>
          </ul>
        )}
  
        {!event && !infoModal && !course && (
          <ul className='modal-title' onClick={handleOpen}>
            {' '}
            {title}
          </ul>
        )}
  
        <Modal
          aria-labelledby='simple-modal-title'
          aria-describedby='simple-modal-description'
          open={open}
          onClose={handleClose}
        >
          <div style={modalStyle} className={classes.paper}>
            <h2 id='simple-modal-title'>{name}</h2>
            <div id='simple-modal-description'>
  
            </div>
            <ModalInfo />
          </div>
        </Modal>
      </div>
    )
  }
  
  export default ModalInfo