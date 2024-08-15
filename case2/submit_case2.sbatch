#!/bin/bash
# ----------------SBATCH Parameters----------------- #
#SBATCH --job-name=case2
#SBATCH --account=gts-cperron7
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=12
#SBATCH --mem-per-cpu=7500M
#SBATCH --time=0:05:00
#SBATCH --qos=embers
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=jyoun39@gatech.edu

# First, go to submit directory
cd ${SLURM_SUBMIT_DIR}

# ----------------Print Some Info------------------- #
echo Running on host `hostname`
echo Using the following nodes:
echo ${SLURM_JOB_NODELIST}
# Compute the number of processors
echo This job has allocated ${SLURM_NTASKS} cores

# -----------------Load Modules--------------------- #
ASDL_BIN="/storage/coda1/p-cperron7/0/cperron7/bin"
source $ASDL_BIN/starccm+/18.02.008-R8/activate

# -------------Environment Variables---------------- #
MACROFILE="case2.java"
SIMFILE="onera-m6-sharp_airfoil.sim"

# -------------Generate Machine File---------------- #
MACHINEFILE="${TMPDIR}/machinefile.${SLURM_JOB_ID}"
# Generate Machinefile for mpi in the same order as if run via srun
srun -l /bin/hostname | sort -n | awk '{print $2}' > ${MACHINEFILE}
echo Machine file written to ${MACHINEFILE}
# Count number of ranks from machine file
SLURM_NTASKS=$(wc -l < ${MACHINEFILE})

# ----------------Execute Script-------------------- #
starccm+ -licpath 27100@ugslic2.ecs.gatech.edu -machinefile ${MACHINEFILE} -np ${SLURM_NTASKS} -batch $MACROFILE $SIMFILE > starccm_${SLURM_JOB_ID}.log