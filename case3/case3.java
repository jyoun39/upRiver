
package macro;

import java.util.*;

import star.common.*;
import star.base.neo.*;

public class case3 extends StarMacro {
    public void execute() {
       execute0();
       execute1();
       execute2();
       executerun();
       }
  private void execute0() {

    Simulation simulation_0 = 
      getActiveSimulation();

    simulation_0.get(GlobalParameterManager.class).createGlobalParameter(ScalarGlobalParameter.class, "Scalar");

    ScalarGlobalParameter scalarGlobalParameter_6 = 
      ((ScalarGlobalParameter) simulation_0.get(GlobalParameterManager.class).getObject("Scalar"));

    scalarGlobalParameter_6.setPresentationName("new1");

    Units units_0 = 
      ((Units) simulation_0.getUnitsManager().getObject(""));

    scalarGlobalParameter_6.getQuantity().setValueAndUnits(0, units_0);
  }

  private void execute1() {

    Simulation simulation_0 = 
      getActiveSimulation();

    simulation_0.get(GlobalParameterManager.class).createGlobalParameter(ScalarGlobalParameter.class, "Scalar");

    ScalarGlobalParameter scalarGlobalParameter_6 = 
      ((ScalarGlobalParameter) simulation_0.get(GlobalParameterManager.class).getObject("Scalar"));

    scalarGlobalParameter_6.setPresentationName("new2");

    Units units_0 = 
      ((Units) simulation_0.getUnitsManager().getObject(""));

    scalarGlobalParameter_6.getQuantity().setValueAndUnits(0.92444, units_0);
  }

  private void execute2() {

    Simulation simulation_0 = 
      getActiveSimulation();

    simulation_0.get(GlobalParameterManager.class).createGlobalParameter(ScalarGlobalParameter.class, "Scalar");

    ScalarGlobalParameter scalarGlobalParameter_6 = 
      ((ScalarGlobalParameter) simulation_0.get(GlobalParameterManager.class).getObject("Scalar"));

    scalarGlobalParameter_6.setPresentationName("new3");

    Units units_0 = 
      ((Units) simulation_0.getUnitsManager().getObject(""));

    scalarGlobalParameter_6.getQuantity().setValueAndUnits(13.0, units_0);
  }

  private void executerun() {
    Simulation simulation_0 = 
      getActiveSimulation();
    simulation_0.getSimulationIterator().run();
  }
}