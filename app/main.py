# Internal imports
from app.models import AnalysisModel, SynthesisModel
from app.views import AnalysisView, SynthesisView
from app.controllers import AnalysisController, SynthesisController
from app.data import OpcodeData


def run():
    print('Welcome, let\'s assemble some assembly!\n')

    # Run analysis on the assembly file and return the synthesis_model
    synthesis_model = AnalysisController(model=AnalysisModel('assembler/asm-2.txt'), view=AnalysisView).run()

    # Set the opcode table in the synthesis model
    synthesis_model.opcode_table = OpcodeData.get_opcode_data()

    # Run the synthesis to generate machine code
    SynthesisController(model=synthesis_model, view=SynthesisView).run()
